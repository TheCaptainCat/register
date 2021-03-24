from bolinette import types, core, mapping
from bolinette.decorators import model, with_mixin


@model('version')
@with_mixin('historized')
class Version(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True, model_id=True)
    content = types.defs.Column(types.db.String, nullable=False)

    page_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('page', 'id'), nullable=False)
    page = types.defs.Relationship('page', foreign_key=page_id,
                                   backref=types.defs.Backref('versions', lazy=False), lazy=True)

    def responses(self):
        base = self.get_mixin('historized').response(self)
        yield [
            mapping.Column(self.content)
        ] + base
