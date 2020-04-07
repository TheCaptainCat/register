from bolinette import mapping, db
from bolinette.models import Historized


class Article(db.defs.model, Historized):
    __tablename__ = 'article'

    id = db.defs.column(db.types.integer, primary_key=True)

    @staticmethod
    def responses():
        base = Historized.base_response()
        yield [
            mapping.Field(db.types.integer, key='id')
        ] + base


mapping.register(Article)
