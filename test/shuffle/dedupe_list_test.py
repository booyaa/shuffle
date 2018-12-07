from src.shuffle import Dedupe

class TestDedupeList:
  def setup(self):
    self.dedupe = Dedupe()

  def test_list_has_dupes(self):
    expected = [1]
    actual = self.dedupe.execute([1,1,1])

    assert expected == actual

  def test_list_has_no_dupes(self):
    expected = [1,2]
    actual = self.dedupe.execute([1,2])

    assert expected == actual
