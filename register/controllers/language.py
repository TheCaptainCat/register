from bolinette import web
from bolinette.decorators import controller


@controller('language', '/lang')
class LanguageController(web.Controller):
    def default_routes(self):
        return [
            self.defaults.get_all(),
            self.defaults.create(middlewares=['auth|roles=creator']),
            self.defaults.delete(middlewares=['auth|roles=creator'])
        ]
