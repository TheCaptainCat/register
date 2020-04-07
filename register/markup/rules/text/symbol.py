from register.markup.cursors import Delimiter
from register.markup.rules.text import Rule


class Symbol(Rule):
    def _close(self, cursor, start, end, symbol):
        pass

    def _find_start(self, cursor, symbol, end):
        index = end - 1
        delimiters = []
        while True:
            if index < 0 or (cursor.char_at(index) == symbol and len(delimiters) == 0):
                break
            char = cursor.char_at(index)
            if isinstance(char, Delimiter):
                if char.closing:
                    delimiters.append(char)
                elif not len(delimiters):
                    break
                else:
                    delimiters.pop()
            index -= 1
        return index

    def process(self, cursor):
        symbol = cursor.char
        left = cursor.get_char(-1)
        if left not in [None, ' '] and left != symbol:
            end = cursor.index
            start = self._find_start(cursor, symbol, end)
            if (start >= 0 and cursor.char_at(start) == symbol
                    and cursor.char_at(start + 1) not in [None, ' ']):
                self._close(cursor, start, end, symbol)
        cursor.inc()


class SingleSymbol(Symbol):
    def __init__(self, symbols, tag):
        self.symbols = symbols
        self.tag = tag

    def test(self, cursor):
        return cursor.char in self.symbols

    def _close(self, cursor, start, end, symbol):
        cursor.line[start] = Delimiter(self.tag, False)
        cursor.line[end] = Delimiter(self.tag, True)


class DoubleSymbol(Symbol):
    def __init__(self, symbols, single_tag, double_tag):
        self.symbols = symbols
        self.single_tag = single_tag
        self.double_tag = double_tag

    def test(self, cursor):
        c = cursor.char
        c2 = cursor.get_char(1)
        return isinstance(c, str) and isinstance(c2, str) and c + c2 in self.symbols

    def _close(self, cursor, start, end, symbol):
        tag = self.single_tag
        if cursor.char_at(start - 1) == symbol:
            tag = self.double_tag
        cursor.line[end] = Delimiter(tag, True)
        cursor.line[start] = Delimiter(tag, False)
        if tag == self.double_tag:
            cursor.sub(end + 1)
            cursor.sub(start - 1)
            cursor.index -= 1
