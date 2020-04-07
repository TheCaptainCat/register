from register.markup.rules.text import Rule


class Character(Rule):
    def test(self, cursor):
        return True

    def process(self, cursor):
        cursor.inc()
