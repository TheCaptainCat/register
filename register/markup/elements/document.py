from register.markup import blocks
from register.markup.elements import Tag


class Document:
    def __init__(self):
        self.blocks = [blocks.Block()]
        self.footnotes = []
        self.tree = Tag('article', None)
        self.notes = None

    @property
    def block(self):
        return self.blocks[-1] if len(self.blocks) > 0 else None

    def commit(self):
        if len(self.block) > 0:
            if isinstance(self.block.type, blocks.FootNote):
                note = self.block
                self.blocks.remove(note)
                self.footnotes.append(note)
            self.blocks.append(blocks.Block())

    def merge(self):
        self.notes = Tag('notes', self.tree)
        for note in self.footnotes:
            tag = note.type.outer_tag(
                self.notes, attrs={'ref': note.type.ref, 'index': note.type.index}
            )
            for line in note.content:
                tag.children.append(line)
    
    def find_footnote(self, ref):
        for note in self.footnotes:
            if note.type.ref == ref:
                return note.type.index
        return None
    
    def add_footnote(self, content):
        note = blocks.Block()
        note.type = blocks.FootNote(f'note{blocks.FootNote.index}')
        tag = note.type.outer_tag(
            self.notes, attrs={'ref': note.type.ref, 'index': note.type.index}
        )
        tag.children.append(content)
        return note.type.ref, note.type.index

    def deep_print(self):
        self.tree.deep_print()
