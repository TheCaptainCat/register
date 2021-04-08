from bolinette import web
from bolinette.decorators import controller, get, post, patch
from bolinette.exceptions import NotFoundError

from register.services import PageService, LanguageService, ArticleService


@controller('page')
class PageController(web.Controller):
    @property
    def language_service(self) -> LanguageService:
        return self.context.service('language')

    @property
    def page_service(self) -> PageService:
        return self.context.service('page')

    @property
    def article_service(self) -> ArticleService:
        return self.context.service('article')

    @get('/{lang}', returns=web.Returns('page', 'list', as_list=True))
    async def get_by_language(self, match):
        """
        Gets all pages associated with a language
        """
        lang = await self.language_service.get_by_name(match['lang'])
        return self.response.ok(data=await self.page_service.get_by_language(lang))

    @post('/{lang}', middlewares=['auth|roles=creator'],
          expects=web.Expects('page', 'new'), returns=web.Returns('page', 'complete'))
    @post('/{lang}/{article}', middlewares=['auth|roles=creator'],
          expects=web.Expects('page', 'new'), returns=web.Returns('page', 'complete'))
    async def create_page(self, payload, match, current_user):
        """
        Creates a new page, with a new article if no article id is given
        """
        language = await self.language_service.get_by_name(match['lang'])
        article_id = match.get('article')
        article = None
        if article_id:
            article = await self.article_service.get_by_key(article_id)
        return self.response.created(
            messages='page.created', data=await self.page_service.add_version(
                payload['name'], payload['content'], article, language, current_user))

    @get('/{lang}/{article}', middlewares=['auth'],
         returns=web.Returns('page', 'complete'))
    async def get_page(self, match):
        """
        Gets a page associated with a language from an article
        """
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get_by_key(match['article'])
        return self.response.ok(data=await self.page_service.get_one_by_article_language(article, language))

    @get('/{lang}/{article}/content', middlewares=['auth'])
    async def get_page_content(self, match):
        """
        Get the parsed content of a page
        """
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get_by_key(match['article'])
        page = await self.page_service.get_one_by_article_language(article, language)
        return self.response.ok(data=await self.page_service.get_parsed_content(page))

    @patch('/{lang}/{article}', middlewares=['auth|roles=creator'],
           expects=web.Expects('page', 'new', patch=True), returns=web.Returns('page', 'complete'))
    async def update_page(self, match, payload, current_user):
        """
        Updates a page, or publishes a new page version
        """
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get_by_key(match['article'])
        page = await self.page_service.get_one_by_article_language(article, language)
        await self.page_service.add_version(page.name, payload.get('content'), article, language, current_user)
        values = {}
        if 'name' in payload:
            values['name'] = payload['name']
        updated = await self.page_service.patch(page, values, current_user=current_user)
        return self.response.ok(messages='page.updated', data=updated)

    @get('/{lang}/{article}/versions', middlewares=['auth'],
         returns=web.Returns('version', 'default', as_list=True))
    async def get_page_versions(self, match):
        """
        Gets the last version of a page
        """
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get_by_key(match['article'])
        page = await self.page_service.get_one_by_article_language(article, language)
        return self.response.ok(data=sorted(page.versions, key=lambda v: v.created_on))

    @get('/{lang}/{article}/versions/{version}', middlewares=['auth'],
         returns=web.Returns('version'))
    async def get_page_version(self, match):
        """
        Gets a specific page version
        """
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get_by_key(match['article'])
        version_index = int(match['version'])
        page = await self.page_service.get_one_by_article_language(article, language)
        versions = sorted(page.versions, key=lambda v: v.created_on)
        if version_index >= len(versions):
            raise NotFoundError(f'page.version.not_found:lang,page,version:{language.name},{page.id},{version_index}')
        return self.response.ok(data=versions[version_index])
