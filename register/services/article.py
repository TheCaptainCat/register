import random
import string

from bolinette import blnt, core
from bolinette.decorators import service


@service('article')
class ArticleService(core.Service):
    def __init__(self, context: 'blnt.BolinetteContext'):
        super().__init__(context)

    async def get_by_language(self, language):
        return [page.article for page in language.pages]

    async def get_by_key(self, key: str):
        return await self.get_first_by('key', key)

    async def create(self, values, *, current_user=None):
        article = True
        key = None
        while article is not None:
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            article = await self.repo.get_first_by('key', key)
        values['key'] = key
        return await super().create(values, current_user=current_user)
