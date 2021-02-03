from bolinette import types, core, mapping
from bolinette.decorators import model, with_mixin, model_property


@model('page')
@with_mixin('historized')
class Page(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True, model_id=True)
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
            mapping.Column(cls.name, required=True),
            mapping.Field(types.db.String, key='content')
        ]

    @classmethod
    def responses(cls):
        base = cls.get_mixin('historized').response(cls)
        yield [
            mapping.Column(cls.name)
        ]
        yield "list", [
            mapping.Column(cls.name),
            mapping.Field(types.db.String, name='language', function=lambda x: x.language.name),
            mapping.Field(types.db.Integer, name='article', function=lambda x: x.article.id)
        ]
        yield 'complete', [
            mapping.Column(cls.name),
            mapping.Field(types.db.Integer, name='version_count', function=lambda page: len(page.versions)),
            mapping.Definition('version', key='last_version'),
            mapping.Definition('article', 'from_page', key='article')
        ] + base
