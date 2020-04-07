from register.markup.cursors import Delimiter
from register.markup.rules.text import DoubleSymbol


class Strong(DoubleSymbol):
    def __init__(self):
        super().__init__(['**', '__'], 'em', 'strong')
