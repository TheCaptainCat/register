import re

from register.markup.rules.blocks import Rule


class Empty(Rule):
    def __init__(self):
        super().__init__(re.compile('^$'))

    def process(self, cursor):
        cursor.commit()
        cursor.inc()
