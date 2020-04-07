from register.markup.blocks import Paragraph


class Block:
    def __init__(self):
        self.content = []
        self.type = Paragraph()

    def append(self, line):
        self.content.append(line)

    def parse(self, rules):
        self.type.parse(self.content, rules)

    def __getitem__(self, index):
        return self.content[index]

    def __repr__(self):
        return f'Block {repr(self.type)} {self.content}'

    def __len__(self):
        return len(self.content)
