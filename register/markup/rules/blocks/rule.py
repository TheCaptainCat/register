from typing import AnyStr, Pattern, Optional, Match


class Rule:
    def __init__(self, pattern: Optional[Pattern[AnyStr]]):
        self.pattern = pattern
        self.match: Optional[Match[AnyStr]] = None

    def test(self, cursor):
        self.match = self.pattern.match(cursor.line)
        return self.match is not None

    def process(self, cursor):
        pass

    def __repr__(self):
        return f'<{type(self).__name__} BlockRule>'
