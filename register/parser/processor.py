from typing import Iterable, Dict, Any, Union
from typing import Optional

import bs4
from bolinette.blnt import BolinetteContext
from bolinette.exceptions import NotFoundError

from register.models import Article
from register.services import ArticleService


class ArticleProcessor:
    def __init__(self, context: BolinetteContext, lang: str):
        self.context = context
        self.lang = lang

    @property
    def article_service(self) -> ArticleService:
        return self.context.service('article')

    async def process(self, html: str):
        soup = bs4.BeautifulSoup(html, features="html.parser")
        return await self._process_tags(soup)

    async def _process_tags(self, soup: bs4.BeautifulSoup):
        tags = []
        async for tag in self._process_children(soup.children):
            tags.append(tag)
        return tags

    async def _process_children(self, tags: Iterable[Union[bs4.Tag, bs4.NavigableString]]):
        for tag in tags:
            if isinstance(tag, bs4.NavigableString):
                if tag.strip():
                    yield await self._process_string(tag)
            elif isinstance(tag, bs4.Tag):
                yield await self._process_tag(tag)

    async def _process_tag(self, tag: bs4.Tag) -> Dict[str, Any]:
        if 'reg-link' in tag.attrs:
            return await self._process_link(tag)
        t = {
            'type': 'tag',
            'tag': tag.name,
            'children': []
        }
        async for child in self._process_children(tag.children):
            t['children'].append(child)
        return t

    async def _process_link(self, tag: bs4.Tag) -> Dict[str, Any]:
        try:
            article = await self.article_service.get_by_key(tag.attrs['reg-link'])  # type: Optional[Article]
        except NotFoundError:
            article = None
        t = {
            'type': 'link',
            'link': None,
            'name': None,
            'children': []
        }
        if article is not None:
            t['link'] = article.key
            for page in article.pages:
                if page.language.name == self.lang:
                    t['name'] = page.name
                    break
        async for child in self._process_children(tag.children):
            t['children'].append(child)
        return t

    async def _process_string(self, string: bs4.NavigableString):
        return {
            'type': 'text',
            'text': string
        }
