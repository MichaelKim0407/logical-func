from logical.boolean import *


def test_const():
    assert true()
    assert not false()


def test_is():
    assert is_true(True)
    assert is_false(False)
    assert not is_true(False)
    assert not is_false(True)
    assert not is_true(1)
    assert not is_false(0)


def test_eval():
    assert eval_true(1)
    assert eval_false(0)
    assert not eval_true(0)
    assert not eval_false(1)
