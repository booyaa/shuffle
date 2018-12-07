from src.shuffle import Sanitize
import pytest

class TestSanitizeList:
  def setup(self):
    self.sanitize = Sanitize()

  def test_empty_is_empty_list(self):
    expected = []
    actual = self.sanitize.execute("")

    assert expected == actual

  def test_comma_is_a_valid_delimiter(self):
    expected = ['1','2','3']
    actual = self.sanitize.execute("1,2,3")

    assert expected == actual

  @pytest.mark.parametrize("input, expected",[
    ("1 2 3", ['1 2 3']),
    ("1.2.3", ['1.2.3']),
    ("1-2-3", ['1-2-3'])
  ])
  def test_everything_else_is_not_valid(self, input, expected):
    assert expected == self.sanitize.execute(input)
