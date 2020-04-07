import re

from register.markup.cursors import Delimiter
from register.markup.rules.text import Rule


class Link(Rule):
    def __init__(self):
        self.pattern = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')

    def test(self, cursor):
        return self.pattern.match(cursor.remaining_line) is not None

    def process(self, cursor):
        match = self.pattern.match(cursor.remaining_line)
        text = match[1]
        link = match[2]
        cursor.line[cursor.index] = Delimiter('a', False, attrs={'href': link})
        cursor.line[cursor.index + len(text) + 1] = Delimiter('a', True)
        cursor.sub(cursor.index + len(text) + 2, len(link) + 2)
        cursor.inc()
