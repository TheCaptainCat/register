import re

from register.markup.cursors import Delimiter
from register.markup.rules.text import Rule


class Footnote(Rule):
    def __init__(self):
        self.pattern = re.compile(r'\[\^([^\]]*)\]')

    def test(self, cursor):
        match = self.pattern.match(cursor.remaining_line)
        ref = match[1] if match is not None else None
        return match is not None and cursor.document.find_footnote(ref) is not None

    def process(self, cursor):
        match = self.pattern.match(cursor.remaining_line)
        ref = match[1]
        index = str(cursor.document.find_footnote(ref))
        cursor.line[cursor.index] = Delimiter('ref', False, attrs={'to': ref})
        cursor.sub(cursor.index + 1, len(ref) + 1)
        cursor.insert(cursor.index + 1, index)
        cursor.line[cursor.index + len(index) + 1] = Delimiter('ref', True)
        cursor.inc(len(index) + 1)
