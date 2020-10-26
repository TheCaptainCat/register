from bolinette import blnt, core
from bolinette.decorators import service


@service('language')
class LanguageService(blnt.Service):
    def __init__(self, context: 'core.BolinetteContext'):
        super().__init__(context)

    async def get_by_name(self, name):
        return await self.get_first_by('name', name)
