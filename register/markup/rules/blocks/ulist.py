import re

from register.markup import blocks
from register.markup.rules.blocks import Rule


class UList(Rule):
    def __init__(self):
        super().__init__(re.compile(r'^( *)([*\-+])+ '))

    def process(self, cursor):
        indent = len(self.match[1])
        symbol = self.match[2]
        if (not isinstance(cursor.block.type, blocks.List)
                or (cursor.block.type.symbol != symbol and cursor.block.type.indent == indent)
                or cursor.block.type.indent > indent
                or cursor.block.type.ordered):
            cursor.commit()
            cursor.block.type = blocks.List(symbol=symbol, indent=indent)
        cursor.push(cursor.line)
        cursor.inc()
