from src.shuffle import Shuffle, Dedupe, Sanitize

class RandomGatewayFake:
  def __init__(self):
    self.was_called = False

  def shuffle(self, list_to_shuffle):
    self.was_called = True
    return list_to_shuffle.reverse()

class TestShuffleList:
  def test_shuffle_list(self):
    expected = ['3','2','1']
    dedupe = Dedupe()
    sanitize = Sanitize()
    random = RandomGatewayFake()
    sut = Shuffle(dedupe, sanitize, random)
    actual = sut.shuffle("1,2,3")
    assert random.was_called == True
    assert expected == actual
