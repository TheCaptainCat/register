from bolinette import mapping, types, core
from bolinette.decorators import model


@model('article', mixins=['historized'])
class Article(core.Model):
    id = types.defs.Column(types.db.Integer, primary_key=True)
    key = types.defs.Column(types.db.String, nullable=False, unique=True, model_id=True)

    def responses(self):
        base = self.get_mixin('historized').response(self)
        yield [
            mapping.Column(self.key)
        ]
        yield "from_page", [
            mapping.Column(self.key),
            mapping.Field(types.db.String, name='languages',
                          function=lambda a: dict(((p.language.name, p.name) for p in a.pages)))
        ]
        yield "complete", [
            mapping.Column(self.key),
            mapping.List(mapping.Definition('page'), key='pages')
        ] + base
