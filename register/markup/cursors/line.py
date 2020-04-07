from register.markup.cursors import Cursor
from register.markup.elements import Tag


class LineCursor(Cursor):
    def __init__(self, document, line):
        super().__init__(document)
        self.line = list(line)
        self.index = 0

    @property
    def char(self):
        return self.get_char(0)

    @property
    def active(self):
        return self.index < len(self.line)

    @property
    def remaining_line(self):
        return ''.join([c for c in self.line[self.index:] if isinstance(c, str)])

    def get_char(self, offset):
        return self.char_at(self.index + offset)

    def char_at(self, index):
        return self.line[index] if 0 <= index < len(self.line) else None

    def inc(self, n=1):
        self.index += n

    def sub(self, index, n=1):
        self.line = self.line[:index] + self.line[index + n:]
    
    def insert(self, index, string):
        self.line = self.line[:index] + list(string) + self.line[index:]

    def merge(self):
        tag = Tag('', None, children=[''])
        for char in self.line:
            if isinstance(char, Delimiter):
                if char.closing:
                    tag.children = [t for t in tag.children if t != '']
                    tag = tag.parent
                    tag.children.append('')
                else:
                    tag = Tag(char.tag, tag, children=[''], attrs=char.attrs)
            else:
                tag.children[-1] += char
        return [t for t in tag.children if t != '']

    def __repr__(self):
        return f'<LineCursor {self.line}>'


class Delimiter:
    def __init__(self, tag, closing, **options):
        self.tag = tag
        self.closing = closing
        self.attrs = options.get('attrs', {})

    def __repr__(self):
        return f'<{self.tag}>' if not self.closing else f'</{self.tag}>'
