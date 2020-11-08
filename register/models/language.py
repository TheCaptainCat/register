from bolinette import types, blnt
from bolinette.decorators import model


@model('language')
class Language(blnt.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    name = types.defs.Column(types.db.String, nullable=False, unique=True)
    default = types.defs.Column(types.db.Boolean, nullable=False, default=False)

    @classmethod
    def payloads(cls):
        yield [
            types.mapping.Column(cls.name, required=True)
        ]

    @classmethod
    def responses(cls):
        yield [
            types.mapping.Column(cls.name),
            types.mapping.Column(cls.default)
        ]
