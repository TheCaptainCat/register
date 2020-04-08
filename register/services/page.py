from bolinette.exceptions import NotFoundError
from bolinette.services import HistorizedService
from sqlalchemy import and_

from register.markup import Parser
from register.models import Page, Article, Version


class PageService(HistorizedService):
    def __init__(self):
        super().__init__(Page)

    async def get_by_language(self, language):
        return await self.get_by('language_id', language.id)

    async def get_by_article(self, article):
        return await self.get_by('article_id', article.id)

    async def get_one_by_article_language(self, article, language):
        criteria = and_(self.model.article_id == article.id, self.model.language_id == language.id)
        pages = await self.get_by_criteria(criteria) or []
        if not len(pages):
            raise NotFoundError(f'page.not_found:lang,article:{language.name},{article.id}')
        return pages[0]

    async def add_version(self, name, content, article, language, current_user, **_):
        if not article:
            article = await self.service(Article).create({}, current_user=current_user)
        try:
            page = await self.get_one_by_article_language(article, language)
        except NotFoundError:
            page = await self.create({'name': name, 'article': article, 'language': language},
                                     current_user=current_user)
        await self.service(Version).create({'content': content, 'page': page}, current_user=current_user)
        return page

    async def get_parsed_content(self, page: Page):
        parser = Parser()
        tree = parser.parse(page.last_version.content)
        return tree.to_dict()


page_service = PageService()
