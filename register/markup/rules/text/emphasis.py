from register.markup.cursors import Delimiter
from register.markup.rules.text import SingleSymbol


class Emphasis(SingleSymbol):
    def __init__(self):
        super().__init__(['*', '_'], 'em')
