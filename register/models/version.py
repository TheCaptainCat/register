from bolinette import blnt, types, core
from bolinette.decorators import model, with_mixin


@model('version')
@with_mixin('historized')
class Version(blnt.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    content = types.defs.Column(types.db.String, nullable=False)

    page_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('page', 'id'), nullable=False)
    page = types.defs.Relationship('page', foreign_key=page_id,
                                   backref=types.defs.Backref('versions', lazy=False), lazy=True)

    era_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('era', 'id'), nullable=False)
    era = types.defs.Relationship('era', foreign_key=era_id, lazy=False)

    @classmethod
    def responses(cls):
        base = core.cache.mixins.get('historized').response(cls)
        yield [
            types.mapping.Column(cls.content)
        ] + base
