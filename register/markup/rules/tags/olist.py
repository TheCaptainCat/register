import re

from register.markup import blocks
from register.markup.elements import Tag
from register.markup.rules.tags import Rule


class OList(Rule):
    def test(self, block):
        return isinstance(block.type, blocks.List) and block.type.ordered

    def process(self, block, parent):
        ol = block.type.outer_tag(parent, attrs={'start': block.type.start})
        for line in block.content:
            li = Tag('li', ol)
            li.children.append(re.sub(r'^ *[\d]+\. ', '', line))
