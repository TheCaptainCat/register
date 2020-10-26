from bolinette import blnt, core


class VersionService(blnt.HistorizedService):
    def __init__(self, context: 'core.BolinetteContext'):
        super().__init__(context)
