from register.markup.cursors import Cursor


class BlockCursor(Cursor):
    def __init__(self, document):
        super().__init__(document)
        self.lines = []
        self.index = 0

    @property
    def active(self):
        return self.index < len(self.lines)

    def inc(self, n=1):
        self.index += n

    @property
    def blocks(self):
        return self.document.blocks

    @property
    def line(self):
        return self.lines[self.index] if self.active else None

    @property
    def previous_block(self):
        return self.blocks[-2] if len(self.blocks) > 1 else None

    @property
    def block(self):
        return self.document.block

    def commit(self):
        self.document.commit()

    def remove_last(self):
        if len(self.blocks) > 0:
            del self.blocks[-1]

    def push(self, line):
        self.block.append(line)

    def read_lines(self, stream):
        line = ''
        for c in stream:
            if c == '\n':
                self.lines.append(line.rstrip())
                line = ''
            else:
                line += c
        if len(line) > 0:
            self.lines.append(line.rstrip())
