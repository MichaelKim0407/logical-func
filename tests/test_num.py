from logical.num import *


def test_integer():
    assert is_integer(1)
    assert is_integer(1.0)
    assert not is_integer(1.1)

    assert not is_not_integer(1)
    assert not is_not_integer(1.0)
    assert is_not_integer(1.1)


def test_div():
    div3 = DivBy(3)
    assert [
               div3(x)
               for x in range(15)
           ] == [True, False, False] * 5


def test_even_odd():
    assert [
               is_even(x)
               for x in range(10)
           ] == [True, False] * 5

    assert [
               is_odd(x)
               for x in range(10)
           ] == [False, True] * 5
