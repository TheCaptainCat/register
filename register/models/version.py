from bolinette import mapping, db
from bolinette.models import Historized


class Version(db.defs.model, Historized):
    __tablename__ = 'version'

    id = db.defs.column(db.types.integer, primary_key=True)
    content = db.defs.column(db.types.string, nullable=False)

    page_id = db.defs.column(db.types.integer, db.types.foreign_key('page', 'id'), nullable=False)

    @staticmethod
    def responses():
        base = Historized.base_response()
        yield [
            mapping.Field(db.types.string, key='content')
        ] + base


mapping.register(Version)
