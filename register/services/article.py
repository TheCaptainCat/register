from bolinette import blnt, core
from bolinette.decorators import service


@service('article')
class ArticleService(core.HistorizedService):
    def __init__(self, context: 'blnt.BolinetteContext'):
        super().__init__(context)

    async def get_by_language(self, language):
        return [page.article for page in language.pages]
