class Mergeable:
    def merge(self, block):
        block.content = [' '.join(map(lambda s: s.strip(), block.content))]
