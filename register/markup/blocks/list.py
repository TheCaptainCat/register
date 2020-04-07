import re

from register.markup.elements import Tag
from register.markup.blocks import Type, Mergeable


class List(Type, Mergeable):
    def __init__(self, **options):
        self.symbol = options.get('symbol', '-')
        self.ordered = options.get('ordered', False)
        self.start = options.get('start', 1)
        self.indent = options.get('indent', 0)

    def outer_tag(self, parent, **options):
        return Tag('ol' if self.ordered else 'ul', parent, **options)

    def merge(self, block):
        pattern = r'^ *[\d]+\. ' if self.ordered else r'^ *[\*\-\+]+ '
        lines = []
        for line in block.content:
            if re.match(pattern, line):
                lines.append(line)
            else:
                lines[-1] += ' ' + line
        block.content = lines

    def __repr__(self):
        return (f'{super().__repr__()} {"O" if self.ordered else "U"}'
                f':{self.indent} {self.start if self.ordered else self.symbol}')
