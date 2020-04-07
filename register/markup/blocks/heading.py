from register.markup.elements import Tag
from register.markup.blocks import Type


class Heading(Type):
    def __init__(self, nesting):
        self.nesting = nesting

    def outer_tag(self, parent, **options):
        return Tag(f'h{min(self.nesting, 6)}', parent, **options)

    def __repr__(self):
        return f'{super().__repr__()} #{self.nesting}'
