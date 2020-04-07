import re

from register.markup.rules.blocks import Rule


class Paragraph(Rule):
    def __init__(self):
        super().__init__(re.compile('^.*$'))

    def process(self, cursor):
        cursor.push(cursor.line)
        cursor.inc()
