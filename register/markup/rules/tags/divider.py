from register.markup import blocks
from register.markup.rules.tags import Rule


class Divider(Rule):
    def test(self, block):
        return isinstance(block.type, blocks.Divider)

    def process(self, block, parent):
        block.type.outer_tag(parent)
