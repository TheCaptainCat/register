from bolinette.services import HistorizedService
from register.models import Version


class VersionService(HistorizedService):
    def __init__(self):
        super().__init__(Version)


version_service = VersionService()
