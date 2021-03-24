from bolinette import blnt, core
from bolinette.decorators import service
from bolinette.exceptions import NotFoundError

from register.markup import Parser


@service('page')
class PageService(core.HistorizedService):
    def __init__(self, context: 'blnt.BolinetteContext'):
        super().__init__(context)

    async def get_by_language(self, language):
        return await self.get_by('language_id', language.id)

    async def get_by_article(self, article):
        return await self.get_by('article_id', article.id)

    async def get_one_by_article_language(self, article, language):
        pages = await (self.repo.query()
                       .filter(lambda p: p.article == article and p.language == language)
                       .all())
        if not len(pages):
            raise NotFoundError(f'page.not_found:lang,article:{language.name},{article.key}')
        return pages[0]

    async def add_version(self, name, content, article, language, current_user, **_):
        if not article:
            article = await self.context.service('article').create({}, current_user=current_user)
        try:
            page = await self.get_one_by_article_language(article, language)
        except NotFoundError:
            page = await self.create({'name': name, 'article': article, 'language': language},
                                     current_user=current_user)
        if content:
            await self.context.service('version').create({'content': content, 'page': page},
                                                         current_user=current_user)
        return page

    async def get_parsed_content(self, page):
        parser = Parser()
        tree = parser.parse(page.last_version.content)
        return tree.to_dict()
