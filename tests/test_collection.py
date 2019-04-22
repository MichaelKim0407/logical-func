from logical.collection import In, Contains


def test_in():
    in_123 = In([1, 2, 3])
    assert in_123(1)
    assert not in_123(4)


def test_contains():
    contains_1 = Contains(1)
    assert contains_1([1, 2, 3])
    assert not contains_1([0, 4])
