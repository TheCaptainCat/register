from register.markup.elements import Tag
from register.markup.blocks import Type, Mergeable


class FootNote(Type, Mergeable):
    index = 1

    def __init__(self, ref):
        self.ref = ref
        self.index = FootNote.index
        FootNote.index += 1

    def outer_tag(self, parent, **options):
        return Tag('footnote', parent, **options)

    def __repr__(self):
        return f'{super().__repr__()} ^{self.ref}'
