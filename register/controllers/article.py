from bolinette import web
from bolinette.decorators import controller, get

from register.services import ArticleService, LanguageService


@controller('article')
class ArticleController(web.Controller):
    @property
    def article_service(self) -> ArticleService:
        return self.context.service('article')

    @property
    def language_service(self) -> LanguageService:
        return self.context.service('language')

    def default_routes(self):
        return [
            self.defaults.get_all('complete', middlewares=['auth'])
        ]

    @get('/{lang}', returns=web.Returns('article', 'default', as_list=True))
    async def get_by_language(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        return self.response.ok('OK', await self.article_service.get_by_language(language))
