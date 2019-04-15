from logical.typing import *


def test_isinstance():
    class C(object):
        pass

    is_c = IsInstance(C)
    assert is_c(C())
    assert not is_c(0)


def test_bool():
    assert is_bool(True)
    assert is_bool(False)
    assert not is_bool(0)
    assert not is_bool('a')


def test_num():
    assert is_int(0)
    assert is_int(1)
    assert not is_int(1.1)
    assert not is_int('1')

    assert is_float(1.1)
    assert not is_float(0)
    assert not is_float('1.1')

    assert is_num(1)
    assert is_num(1.1)
    assert not is_num('1.1')


def test_str():
    assert is_str('')
    assert is_str('1')
    assert not is_str(1)
    assert not is_str(b'')

    assert is_bytes(b'')
    assert is_bytes(b'1')
    assert not is_bytes(1)
    assert not is_bytes('')

    assert is_any_str('1')
    assert is_any_str(b'1')
    assert not is_any_str(1)
