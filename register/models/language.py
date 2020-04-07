from bolinette import mapping, db


class Language(db.defs.model):
    __tablename__ = 'language'

    id = db.defs.column(db.types.integer, primary_key=True)
    name = db.defs.column(db.types.string, nullable=False, unique=True)

    @staticmethod
    def payloads():
        yield [
            mapping.Field(db.types.string, key='name', required=True)
        ]

    @staticmethod
    def responses():
        yield [
            mapping.Field(db.types.string, key='name')
        ]


mapping.register(Language)
