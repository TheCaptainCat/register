from register.markup.cursors import Delimiter
from register.markup.rules.text import SingleSymbol


class Subscript(SingleSymbol):
    def __init__(self):
        super().__init__(['~'], 'sub')
