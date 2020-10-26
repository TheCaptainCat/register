from bolinette import blnt, types
from bolinette.decorators import controller


@controller('language')
class LanguageController(blnt.Controller):
    def default_routes(self):
        return [
            self.defaults.get_all(access=types.web.AccessToken.Required),
            self.defaults.get_one('complete', access=types.web.AccessToken.Required),
            self.defaults.create(access=types.web.AccessToken.Required, roles=['admin']),
            self.defaults.update(access=types.web.AccessToken.Required, roles=['admin']),
            self.defaults.delete(access=types.web.AccessToken.Required, roles=['admin'])
        ]
