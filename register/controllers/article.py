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

    @get('/a/{article}/languages', middlewares='auth')
    async def get_languages(self, match):
        article = await self.article_service.get_by_key(match['article'])
        languages = {}
        for page in article.pages:
            languages[page.language.name] = page.name
        return self.response.ok(data=languages)
