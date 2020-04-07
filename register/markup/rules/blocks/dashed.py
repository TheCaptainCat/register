import re

from register.markup.blocks import Divider, Paragraph, Heading
from register.markup.rules.blocks import Rule


class Dashed(Rule):
    def __init__(self):
        super().__init__(re.compile(r'^ *[\-*_]{3}$'))
        self.heading_pattern = re.compile(r'^ *[\-=]+$')

    def _hr_test(self, cursor):
        return self.pattern.match(cursor.line)

    def _heading_test(self, cursor):
        return (cursor.block is not None and len(cursor.block) == 1
                and isinstance(cursor.block.type, Paragraph)
                and self.heading_pattern.match(cursor.line))

    def test(self, cursor):
        return self._heading_test(cursor) or self._hr_test(cursor)

    def process(self, cursor):
        if self._heading_test(cursor):
            c = cursor.line.strip()[0]
            cursor.block.type = Heading(1 if c == '=' else 2)
            cursor.commit()
        elif self._hr_test(cursor):
            cursor.commit()
            cursor.push(cursor.line.strip())
            cursor.block.type = Divider()
        cursor.commit()
        cursor.inc()
