# This is a very simple unit test just for the sake of having one
from counter import increment_count

def test_increment():
    assert 2 == increment_count(1)