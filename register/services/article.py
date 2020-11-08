from bolinette import blnt, core
from bolinette.decorators import service


@service('article')
class ArticleService(blnt.HistorizedService):
    def __init__(self, context: 'core.BolinetteContext'):
        super().__init__(context)

    async def get_by_language(self, language):
        return [page.article for page in language.pages]
