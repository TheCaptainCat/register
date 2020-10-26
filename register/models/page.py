from bolinette import blnt, types, core
from bolinette.decorators import model, with_mixin, model_property


@model('page')
@with_mixin('historized')
class Page(blnt.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    name = types.defs.Column(types.db.String, nullable=False)

    article_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('article', 'id'), nullable=False)
    article = types.defs.Relationship('article', foreign_key=article_id, lazy=False)

    language_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('language', 'id'), nullable=False)
    language = types.defs.Relationship('language', foreign_key=language_id, lazy=False)

    @model_property
    def last_version(self):
        versions = sorted(self.versions, key=lambda v: v.created_on, reverse=True)
        return versions[0]

    @classmethod
    def payloads(cls):
        yield 'new', [
            types.mapping.Column(cls.name, required=True),
            types.mapping.Field(types.db.String, key='content', required=True)
        ]
        yield 'version', [
            types.mapping.Field(types.db.String, key='content', required=True)
        ]

    @classmethod
    def responses(cls):
        base = core.cache.mixins.get('historized').response(cls)
        yield [
            types.mapping.Column(cls.name)
        ] + base
        yield 'complete', [
            types.mapping.Column(cls.name),
            types.mapping.Field(types.db.Integer, name='version_count', function=lambda page: len(page.versions)),
            types.mapping.Definition('version', key='last_version')
        ] + base
