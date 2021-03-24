from bolinette import core, mapping, types
from bolinette.decorators import model


@model('language')
class Language(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    name = types.defs.Column(types.db.String, nullable=False, unique=True, model_id=True)
    default = types.defs.Column(types.db.Boolean, nullable=False, default=False)

    def payloads(self):
        yield [
            mapping.Column(self.name, required=True)
        ]

    def responses(self):
        yield [
            mapping.Column(self.name),
            mapping.Column(self.default)
        ]
