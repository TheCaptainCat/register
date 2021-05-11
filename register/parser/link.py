from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as ETree


class LinkInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md):
        super().__init__(pattern, md)

    def handleMatch(self, m, data):
        el = ETree.Element('a')
        el.text = m.group(2)
        el.set('reg-link', m.group(1))
        return el, m.start(0), m.end(0)


class LinkExtension(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.inlinePatterns.register(
            LinkInlineProcessor(r'@\[#([a-zA-Z0-9]+)\|([^\]]+)\]', md), 'del', 175)
