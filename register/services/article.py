from bolinette.services import HistorizedService
from register.models import Article


class ArticleService(HistorizedService):
    def __init__(self):
        super().__init__(Article)


article_service = ArticleService()
