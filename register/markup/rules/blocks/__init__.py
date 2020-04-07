from register.markup.rules.blocks.rule import Rule
from register.markup.rules.blocks.dashed import Dashed
from register.markup.rules.blocks.empty import Empty
from register.markup.rules.blocks.heading import Heading
from register.markup.rules.blocks.olist import OList
from register.markup.rules.blocks.paragraph import Paragraph
from register.markup.rules.blocks.quote import Quote
from register.markup.rules.blocks.footnote import FootNote
from register.markup.rules.blocks.ulist import UList


def load_rules():
    return [
        Empty(),
        Heading(),
        Dashed(),
        Quote(),
        UList(),
        OList(),
        FootNote(),
        Paragraph()
    ]
