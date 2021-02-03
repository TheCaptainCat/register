from bolinette import mapping, types, core
from bolinette.decorators import model, with_mixin


@model('article')
@with_mixin('historized')
class Article(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True, model_id=True)

    @classmethod
    def responses(cls):
        base = cls.get_mixin('historized').response(cls)
        yield [
            mapping.Column(cls.id)
        ]
        yield "from_page", [
            mapping.Column(cls.id),
            mapping.Field(types.db.String, name='languages',
                          function=lambda a: [p.language.name for p in a.pages])
        ]
        yield "complete", [
            mapping.Column(cls.id),
            mapping.List(mapping.Definition('page'), key='pages')
        ] + base
