from logical import Function

div3 = Function(lambda x: x % 3 == 0)
div5 = Function(lambda x: x % 5 == 0)


def test_call():
    assert [
               div3(x)
               for x in range(15)
           ] == [True, False, False] * 5

    assert [
               div5(x)
               for x in range(15)
           ] == [True, False, False, False, False] * 3


def test_invert():
    ndiv3 = ~div3
    ndiv5 = ~div5

    assert [
               ndiv3(x)
               for x in range(15)
           ] == [False, True, True] * 5

    assert [
               ndiv5(x)
               for x in range(15)
           ] == [False, True, True, True, True] * 3


def test_invert_same():
    ndiv3 = ~div3
    ndiv5 = ~div5

    assert (~ndiv3) is div3
    assert (~ndiv5) is div5


def test_and():
    div3and5 = div3 & div5

    assert [
               div3and5(x)
               for x in range(15)
           ] == [
               True, False, False,
               False, False, False,
               False, False, False,
               False, False, False,
               False, False, False,
           ]


def test_or():
    div3or5 = div3 | div5

    assert [
               div3or5(x)
               for x in range(15)
           ] == [
               True, False, False,
               True, False, True,
               True, False, False,
               True, True, False,
               True, False, False,
           ]
