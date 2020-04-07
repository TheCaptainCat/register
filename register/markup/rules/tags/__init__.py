from register.markup.rules.tags.rule import Rule
from register.markup.rules.tags.default import Default
from register.markup.rules.tags.quote import Quote
from register.markup.rules.tags.divider import Divider
from register.markup.rules.tags.olist import OList
from register.markup.rules.tags.ulist import UList


def load_rules():
    return [
        OList(),
        UList(),
        Divider(),
        Quote(),
        Default()
    ]
