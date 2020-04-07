import re

from register.markup import blocks
from register.markup.elements import Tag
from register.markup.rules.tags import Rule


class UList(Rule):
    def test(self, block):
        return isinstance(block.type, blocks.List) and not block.type.ordered

    def _count_indent(self, line):
        i = 0
        for c in line:
            if c != ' ':
                break
            else:
                i += 1
        return i - (i % 2)

    def process(self, block, parent):
        ul = block.type.outer_tag(parent, )
        levels = []
        for line in block.content:
            indent = self._count_indent(line)
            if not len(levels):
                levels.append(indent)
            elif indent > levels[-1]:
                levels.append(indent)
                ul = Tag('ul', ul.children[-1])
            elif indent < levels[-1]:
                while len(levels) > 0 and indent <= levels[-1]:
                    levels.pop()
                if not len(levels) or indent > levels[-1]:
                    levels.append(indent)
                ul = ul.parent.parent
            li = Tag('li', ul)
            li.children.append(re.sub(r'^ *[\-+*] ', '', line))
