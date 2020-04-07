class Type:
    def outer_tag(self, parent, **options):
        pass

    def parse(self, lines, rules):
        print(lines, rules)

    def __repr__(self):
        return f'{type(self).__name__}'
