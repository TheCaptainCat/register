from register.markup import blocks
from register.markup.rules.tags import Rule


class Quote(Rule):
    def test(self, block):
        return isinstance(block.type, blocks.Quote)

    def process(self, block, parent):
        tag = parent
        for i in range(0, block.type.nesting):
            tag = block.type.outer_tag(tag)
        tag.children.append(block.content[0])
