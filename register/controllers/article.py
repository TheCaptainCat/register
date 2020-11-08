from bolinette import blnt, types
from bolinette.decorators import controller, get

from register.services import ArticleService, LanguageService


@controller('article')
class ArticleController(blnt.Controller):
    @property
    def article_service(self) -> ArticleService:
        return self.context.service('article')

    @property
    def language_service(self) -> LanguageService:
        return self.context.service('language')

    def default_routes(self):
        return [
            self.defaults.get_all('complete', access=types.web.AccessToken.Required)
        ]

    @get('/{lang}', returns=('article', 'default', 'as_list'))
    async def get_by_language(self, match):
        language = await self.language_service.get_by_name(match['lang'])
        return self.response.ok('OK', await self.article_service.get_by_language(language))
