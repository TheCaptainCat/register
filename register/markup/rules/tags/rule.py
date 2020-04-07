class Rule:
    def test(self, block):
        pass

    def process(self, block, parent):
        pass

    def __repr__(self):
        return f'<{type(self).__name__} TagRule>'
