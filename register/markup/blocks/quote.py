from register.markup.elements import Tag
from register.markup.blocks import Type, Mergeable


class Quote(Type, Mergeable):
    def __init__(self, nesting):
        self.nesting = nesting

    def outer_tag(self, parent, **options):
        return Tag('blockquote', parent, **options)

    def __repr__(self):
        return f'{super().__repr__()} #{self.nesting}'
