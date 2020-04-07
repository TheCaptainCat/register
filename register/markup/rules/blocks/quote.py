import re

from register.markup import blocks
from register.markup.rules.blocks import Rule


class Quote(Rule):
    def __init__(self):
        super().__init__(re.compile(r'^( *>)+ '))

    def process(self, cursor):
        cursor.commit()
        cursor.push(self.pattern.sub('', cursor.line))
        n = self.match.group(0).count('>')
        cursor.block.type = blocks.Quote(n)
        cursor.inc()
