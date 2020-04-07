import re

from register.markup.cursors import Delimiter
from register.markup.rules.text import Rule


class InlineFootnote(Rule):
    def __init__(self):
        self.pattern = re.compile(r'\^\[([^\]]*)\]')

    def test(self, cursor):
        return self.pattern.match(cursor.remaining_line) is not None

    def process(self, cursor):
        match = self.pattern.match(cursor.remaining_line)
        content = match[1]
        ref, index = cursor.document.add_footnote(content)
        index = str(index)
        cursor.line[cursor.index] = Delimiter('ref', False, attrs={'to': ref})
        cursor.sub(cursor.index + 1, len(content) + 1)
        cursor.insert(cursor.index + 1, index)
        cursor.line[cursor.index + len(index) + 1] = Delimiter('ref', True)
        cursor.inc(len(index) + 1)
