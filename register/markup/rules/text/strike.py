from register.markup.cursors import Delimiter
from register.markup.rules.text import DoubleSymbol


class Strike(DoubleSymbol):
    def __init__(self):
        super().__init__(['~~'], 'sub', 's')
