from logical.comparison import *


def test_equal():
    eq3 = Equal(3)
    assert [
               eq3(x)
               for x in range(5)
           ] == [False, False, False, True, False]


def test_lt():
    lt3 = LessThan(3)
    assert [
               lt3(x)
               for x in range(5)
           ] == [True, True, True, False, False]


def test_gt():
    gt3 = GreaterThan(3)
    assert [
               gt3(x)
               for x in range(5)
           ] == [False, False, False, False, True]


def test_le():
    le3 = LessThanOrEqual(3)
    assert [
               le3(x)
               for x in range(5)
           ] == [True, True, True, True, False]


def test_ge():
    ge3 = GreaterThanOrEqual(3)
    assert [
               ge3(x)
               for x in range(5)
           ] == [False, False, False, True, True]
