from bolinette import core, mapping, types
from bolinette.decorators import model


@model('language')
class Language(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    name = types.defs.Column(types.db.String, nullable=False, unique=True, model_id=True)
    default = types.defs.Column(types.db.Boolean, nullable=False, default=False)

    @classmethod
    def payloads(cls):
        yield [
            mapping.Column(cls.name, required=True)
        ]

    @classmethod
    def responses(cls):
        yield [
            mapping.Column(cls.name),
            mapping.Column(cls.default)
        ]
