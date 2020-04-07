import re

from register.markup import blocks
from register.markup.rules.blocks import Rule


class OList(Rule):
    def __init__(self):
        super().__init__(re.compile(r'^( *)(\d+)\. '))

    def process(self, cursor):
        start = int(self.match[2])
        if (not isinstance(cursor.block.type, blocks.List)
                or not cursor.block.type.ordered):
            cursor.commit()
            cursor.block.type = blocks.List(start=start, indent=0, ordered=True)
        cursor.push(cursor.line)
        cursor.inc()
