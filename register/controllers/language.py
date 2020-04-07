from bolinette.routing import Namespace, AccessType
from register.services import language_service

ns = Namespace('/language', language_service)

ns.defaults.get_all(access=AccessType.Required)
ns.defaults.get_one('complete', access=AccessType.Required)
ns.defaults.create()
ns.defaults.update(access=AccessType.Required, roles=['admin'])
ns.defaults.delete(access=AccessType.Required, roles=['admin'])
