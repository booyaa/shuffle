import random
from collections import OrderedDict

class Shuffle:
    def __init__(self, dedupe, sanitize, shuffler=random):
        self.returned_list = []
        self.dedupe = dedupe
        self.sanitize = sanitize
        self.shuffler = shuffler

    def shuffle(self, list_to_shuffle):
        self.returned_list = self.sanitize.execute(list_to_shuffle)
        self.returned_list = self.dedupe.execute(self.returned_list)
        self.shuffler.shuffle(self.returned_list)
        return self.returned_list

class Dedupe:
    def execute(self, list_to_dedupe):
        deduped = list(OrderedDict.fromkeys(list_to_dedupe))
        return deduped


class Sanitize:
    def execute(self, list_to_sanitize):
        split_list = list_to_sanitize.split(',')
        sanitized = list(filter(lambda x: len(x) > 0, split_list))
        return sanitized
