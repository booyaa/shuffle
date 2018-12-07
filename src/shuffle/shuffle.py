import random

class Shuffle:
  def __init__(self,dedupe,sanitize):
    self.returned_list = []
    self.dedupe = dedupe
    self.sanitize = sanitize

  def shuffle(self, list_to_shuffle):
    self.returned_list = self.dedupe.execute(self.sanitize.execute(list_to_shuffle))
    random.shuffle(self.returned_list)
    return self.returned_list

class Dedupe:
  def execute(self, list_to_dedupe):
    return list(set(list_to_dedupe))

class Sanitize:
  def execute(self, list_to_sanitize):
    split_list = list_to_sanitize.split(',')
    sanitized = list(filter(lambda x: len(x) > 0, split_list))
    return sanitized
