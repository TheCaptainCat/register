from bolinette import blnt, types, core
from bolinette.decorators import model, with_mixin, model_property


@model('page')
@with_mixin('historized')
class Page(blnt.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    name = types.defs.Column(types.db.String, nullable=False)

    article_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('article', 'id'), nullable=False)
    article = types.defs.Relationship('article', foreign_key=article_id, lazy=False,
                                      backref=types.defs.Backref('pages', lazy=True))

    language_id = types.defs.Column(types.db.Integer, reference=types.defs.Reference('language', 'id'), nullable=False)
    language = types.defs.Relationship('language', foreign_key=language_id, lazy=False,
                                       backref=types.defs.Backref('pages', lazy=True))

    @model_property
    def last_version(self):
        if not len(self.versions):
            return None
        versions = sorted(self.versions, key=lambda v: v.created_on, reverse=True)
        return versions[0]

    @classmethod
    def payloads(cls):
        yield 'new', [
            types.mapping.Column(cls.name, required=True),
            types.mapping.Field(types.db.String, key='content')
        ]

    @classmethod
    def responses(cls):
        base = core.cache.mixins.get('historized').response(cls)
        yield [
            types.mapping.Column(cls.name)
        ]
        yield "list", [
            types.mapping.Column(cls.name),
            types.mapping.Field(types.db.String, name='language', function=lambda x: x.language.name),
            types.mapping.Field(types.db.Integer, name='article', function=lambda x: x.article.id)
        ]
        yield 'complete', [
            types.mapping.Column(cls.name),
            types.mapping.Field(types.db.Integer, name='version_count', function=lambda page: len(page.versions)),
            types.mapping.Definition('version', key='last_version'),
            types.mapping.Definition('article', 'from_page', key='article')
        ] + base
