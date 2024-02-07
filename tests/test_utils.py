from utils import foo, bar


def test_foo():
    assert foo(3, 2) == 5


def test_bar():
    assert bar(2, 3) == 6
