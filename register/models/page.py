from bolinette import mapping, db
from bolinette.models import Historized

from register.models import Article, Language, Version


class Page(db.defs.model, Historized):
    __tablename__ = 'page'

    id = db.defs.column(db.types.integer, primary_key=True)
    name = db.defs.column(db.types.string, nullable=False)

    article_id = db.defs.column(db.types.integer, db.types.foreign_key('article', 'id'), nullable=False)
    article = db.defs.relationship(Article, foreign_keys=article_id, lazy=False)

    language_id = db.defs.column(db.types.integer, db.types.foreign_key('language', 'id'), nullable=False)
    language = db.defs.relationship(Language, foreign_keys=language_id, lazy=False)

    versions = db.defs.relationship(Version, backref=db.defs.backref('page', lazy=True))

    @property
    def last_version(self) -> Version:
        versions = sorted(self.versions, key=lambda v: v.created_on, reverse=True)
        return versions[0]

    @staticmethod
    def payloads():
        yield 'new', [
            mapping.Field(db.types.string, key='name', required=True),
            mapping.Field(db.types.string, key='content', required=True)
        ]
        yield 'version', [
            mapping.Field(db.types.string, key='content', required=True)
        ]

    @staticmethod
    def responses():
        base = Historized.base_response()
        yield [
            mapping.Field(db.types.string, key='name')
        ] + base
        yield 'complete', [
            mapping.Field(db.types.string, key='name'),
            mapping.Field(db.types.integer, name='version_count', function=lambda page: len(page.versions)),
            mapping.Definition('version', key='last_version')
        ] + base


mapping.register(Page)
