from bolinette import blnt, types
from bolinette.decorators import controller, get, post
from bolinette.exceptions import NotFoundError


@controller('page')
class PageController(blnt.Controller):
    @property
    def language_service(self):
        return self.context.service('language')

    @property
    def page_service(self):
        return self.context.service('page')

    @property
    def article_service(self):
        return self.context.service('article')

    @get('/{lang}', access=types.web.AccessToken.Required)
    async def get_by_language(self, match):
        lang = await self.language_service.get_by_name(match['lang'])
        return self.response.ok('OK', await self.page_service.get_by_language(lang))

    @post('/{lang}', access=types.web.AccessToken.Required, roles=['creator'],
          expects=('page', 'new'), returns=('page', 'complete'))
    @post(r'/{lang}/{article:\d+}', access=types.web.AccessToken.Required, roles=['creator'],
          expects=('page', 'version'), returns=('page', 'complete'))
    async def create_page(self, payload, match, current_user):
        language = await self.language_service.get_by_name(match['lang'])
        article_id = match.get('article')
        article = None
        if article_id:
            article = await self.article_service.get(article_id)
        return self.response.created(
            'page.created', await self.page_service.add_version(
                payload.get('name'), payload['content'], article, language, current_user
            )
        )

    @get(r'/{lang}/{article:\d+}', access=types.web.AccessToken.Required,
         returns=('page', 'complete'))
    async def get_page(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get(match['article'])
        return self.response.ok('OK', await self.page_service.get_one_by_article_language(article, language))

    @get(r'/{lang}/{article:\d+}/content', access=types.web.AccessToken.Required)
    async def get_page_content(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get(match['article'])
        page = await self.page_service.get_one_by_article_language(article, language)
        return self.response.ok('OK', await self.page_service.get_parsed_content(page))

    @get(r'/{lang}/{article:\d+}/versions', access=types.web.AccessToken.Required,
         returns=('version', 'default', 'as_list'))
    async def get_page_versions(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get(match['article'])
        page = await self.page_service.get_one_by_article_language(article, language)
        return self.response.ok('OK', sorted(page.versions, key=lambda v: v.created_on))

    @get(r'/{lang}/{article:\d+}/versions/{version:\d+}', access=types.web.AccessToken.Required,
         returns='version')
    async def get_page_version(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        article = await self.article_service.get(match['article'])
        version_index = int(match['version'])
        page = await self.page_service.get_one_by_article_language(article, language)
        versions = sorted(page.versions, key=lambda v: v.created_on)
        if version_index >= len(versions):
            raise NotFoundError(f'page.version.not_found:lang,page,version:{language.name},{page.id},{version_index}')
        return self.response.ok('OK', versions[version_index])
