class Rule:
    def test(self, cursor):
        pass

    def process(self, cursor):
        pass

    def __repr__(self):
        return f'<{type(self).__name__} TextRule>'
