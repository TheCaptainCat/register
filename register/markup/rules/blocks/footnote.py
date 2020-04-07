import re

from register.markup import blocks
from register.markup.rules.blocks import Rule


class FootNote(Rule):
    def __init__(self):
        super().__init__(re.compile(r'^\[\^([^\]]+)\]: '))

    def process(self, cursor):
        cursor.commit()
        cursor.push(self.pattern.sub('', cursor.line))
        ref = self.match.group(1)
        cursor.block.type = blocks.FootNote(ref)
        cursor.inc()
