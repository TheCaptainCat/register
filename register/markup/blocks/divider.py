from register.markup.elements import Tag
from register.markup.blocks import Type


class Divider(Type):
    def outer_tag(self, parent, **options):
        return Tag('hr', parent, **options)
