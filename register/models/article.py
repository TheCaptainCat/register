from bolinette import blnt, types, core
from bolinette.decorators import model, with_mixin


@model('article')
@with_mixin('historized')
class Article(blnt.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)

    @classmethod
    def responses(cls):
        base = core.cache.mixins.get('historized').response(cls)
        yield [
            types.mapping.Column(cls.id)
        ]
        yield "from_page", [
            types.mapping.Column(cls.id),
            types.mapping.Field(types.db.String, name='languages',
                                function=lambda a: [p.language.name for p in a.pages])
        ]
        yield "complete", [
            types.mapping.Column(cls.id),
            types.mapping.List(types.mapping.Definition('page'), key='pages')
        ] + base
