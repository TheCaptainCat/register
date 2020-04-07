class Tag:
    def __init__(self, tag, parent, **options):
        self.tag = tag
        self.parent = parent
        if parent:
            parent.children.append(self)
        self.children = options.get('children', [])
        self.symbol = options.get('symbol')
        self.classes = options.get('classes', [])
        self.attrs = options.get('attrs', {})

    def push(self, tag):
        self.children.append(tag)

    def _str_attrs(self):
        attrs = ' '.join([f'{att}="{value}"' for att, value in self.attrs.items()])
        return ' ' + attrs if len(attrs) > 0 else attrs

    def deep_print(self, n=0):
        print('  ' * n, '<', self.tag, f'{self._str_attrs()}>', sep='')
        for child in self.children:
            if isinstance(child, str):
                print('  ' * (n + 1) + child)
            else:
                child.deep_print(n + 1)
        print('  ' * n, '</', self.tag, '>', sep='')

    def __repr__(self):
        return f'<{self.tag}>'
