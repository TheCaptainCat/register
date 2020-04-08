from register.markup import blocks
from register.markup.cursors import BlockCursor, LineCursor
from register.markup.elements import Tag, Document
from register.markup.rules import blocks as r_blocks, text as r_text, tags as r_tags, Escape


class Parser:
    def __init__(self):
        self.document = Document()
        self.block_cursor = BlockCursor(self.document)
        self.escape = Escape()
        self.block_rules = r_blocks.load_rules()
        self.tag_rules = r_tags.load_rules()
        self.line_rules = r_text.load_rules()

    def parse(self, stream):
        self.block_cursor.read_lines(stream)
        self.escape_chars()
        self.parse_blocks()
        self.document.merge()
        self.parse_text_lines(self.document.tree)
        return self.document.tree

    def escape_chars(self):
        for i in range(len(self.block_cursor.lines)):
            self.block_cursor.lines[i] = self.escape.escape_line(self.block_cursor.lines[i])

    def parse_blocks(self):
        while self.block_cursor.active:
            for rule in self.block_rules:
                if rule.test(self.block_cursor):
                    rule.process(self.block_cursor)
                    break
        self.block_cursor.commit()
        if not len(self.block_cursor.block):
            self.block_cursor.remove_last()
        for block in [block for block in self.block_cursor.blocks
                      if issubclass(type(block.type), blocks.Mergeable)]:
            block.type.merge(block)
        for block in self.block_cursor.blocks:
            for rule in self.tag_rules:
                if rule.test(block):
                    rule.process(block, self.document.tree)
                    break

    def parse_text_lines(self, tag):
        i = 0
        while i < len(tag.children):
            if isinstance(tag.children[i], str):
                cursor = LineCursor(self.document, tag.children[i])
                while cursor.active:
                    for rule in self.line_rules:
                        if rule.test(cursor):
                            rule.process(cursor)
                            break
                tags = cursor.merge()
                for t in tags:
                    if isinstance(t, Tag):
                        t.parent = tag
                tag.children = tag.children[:i] + tags + tag.children[i + 1:]
                i += len(tags)
            else:
                self.parse_text_lines(tag.children[i])
                i += 1
