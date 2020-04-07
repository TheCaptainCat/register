from register.markup.elements import Tag
from register.markup.blocks import Type, Mergeable


class Paragraph(Type, Mergeable):
    def outer_tag(self, parent, **options):
        return Tag('p', parent, **options)
