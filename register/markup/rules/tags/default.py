from register.markup.rules.tags import Rule


class Default(Rule):
    def test(self, block):
        return True

    def process(self, block, parent):
        tag = block.type.outer_tag(parent)
        tag.children.append(block.content[0])
