from hypothesis.core import given
from hypothesis.strategies import integers

from algorithms.chapter_08_dynamic_programming.q011_coins import get_coins
from algorithms.chapter_08_dynamic_programming.q05_multiply import multiply


@given(integers(min_value=0), integers(min_value=0))
def test_multiply(x, y):
    assert multiply(x, y) == x * y


@given(integers(min_value=0, max_value=100))
def test_coins(x):
    possible_coins = [25, 10, 5, 1]
    coins = get_coins(x, possible_coins)
    assert len(coins) == len(set([tuple(l) for l in coins]))
    assert all(sum(l) == x for l in coins)
