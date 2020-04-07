from register.markup.rules.text.rule import Rule
from register.markup.rules.text.symbol import Symbol, SingleSymbol, DoubleSymbol
from register.markup.rules.text.link import Link
from register.markup.rules.text.character import Character
from register.markup.rules.text.emphasis import Emphasis
from register.markup.rules.text.superscript import Superscript
from register.markup.rules.text.strike import Strike
from register.markup.rules.text.subscript import Subscript
from register.markup.rules.text.strong import Strong
from register.markup.rules.text.footnote import Footnote
from register.markup.rules.text.inline_note import InlineFootnote


def load_rules():
    return [
        Link(),
        Strong(),
        Emphasis(),
        Strike(),
        Subscript(),
        Superscript(),
        Footnote(),
        InlineFootnote(),
        Character()
    ]
