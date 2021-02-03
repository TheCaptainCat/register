from bolinette import blnt, core
from bolinette.decorators import service


@service('version')
class VersionService(core.HistorizedService):
    def __init__(self, context: 'blnt.BolinetteContext'):
        super().__init__(context)
