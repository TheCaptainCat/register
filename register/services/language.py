from bolinette.services import BaseService
from register.models import Language


class LanguageService(BaseService):
    def __init__(self):
        super().__init__(Language)

    async def get_by_name(self, name):
        return await self.get_first_by('name', name)


language_service = LanguageService()
