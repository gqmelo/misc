import pytest

from algorithms.chapter_02_linked_lists.common import Node
from algorithms.chapter_02_linked_lists.q01_remove_dups import remove_dups
from algorithms.chapter_02_linked_lists.q02_kth_to_last import get_kth_to_last, \
    get_kth_to_last_recursive
from algorithms.chapter_02_linked_lists.q03_delete_node import delete_node
from algorithms.chapter_02_linked_lists.q04_partition import partition, \
    partition_book
from algorithms.chapter_02_linked_lists.q05_sum_lists import \
    sum_lists_least_significant_first, \
    sum_lists_least_significant_first_iterative


def linked_list(iterable):
    if not len(iterable):
        return None
    head = None
    previous = None
    for item in iterable:
        node = Node(item)
        if not head:
            head = node
        else:
            previous.next = node
        previous = node

    return head


def test_list_to_linked_list():
    assert list(linked_list([4, 3, 6, 7, 8])) == [4, 3, 6, 7, 8]


@pytest.mark.parametrize(
    'original,expected',
    [
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 1, 3, 2, 1], [1, 2, 3]),
    ]
)
def test_remove_dups(original, expected):
    assert list(remove_dups(linked_list(original))) == expected


@pytest.mark.parametrize(
    'kth,expected',
    [
        (1, 1),
        (2, 2),
        (3, 10),
        (4, 5),
        (5, 8),
        (6, 5),
        (7, 3),
    ]
)
@pytest.mark.parametrize('func', [get_kth_to_last, get_kth_to_last_recursive])
def test_get_kth_to_last(kth, expected, func):
    data = [3, 5, 8, 5, 10, 2, 1]
    assert func(linked_list(data), kth).data == expected


@pytest.mark.parametrize(
    'original,expected,value',
    [
        ([1, 2, 3], [1, 3], 2),
        ([3, 5, 8, 5, 10, 2, 1], [3, 5, 8, 5, 10, 1], 2),
    ]
)
def test_delete_middle_node(original, expected, value):
    ll = linked_list(original)
    node = ll
    while node.data != value:
        node = node.next
    delete_node(node)
    assert list(ll) == expected


@pytest.mark.parametrize(
    'original,expected,value',
    [
        ([1], [1], 1),
        ([1, 2, 3], [1, 2, 3], 2),
        ([3, 2, 1], [3, 2, 1], 1),
        ([3, 2, 1], [1, 3, 2], 2),
        ([3, 2, 1], [1, 2, 3], 3),
        ([3, 5, 8, 5, 10, 2, 1], [1, 2, 3, 5, 8, 5, 10], 5),
    ]
)
def test_partition(original, expected, value):
    assert list(partition(linked_list(original), value)) == expected
    # assert list(partition_book(linked_list(original), value)) == expected


@pytest.mark.parametrize(
    'l1,l2,expected',
    [
        ([1], [1], [2]),
        ([2, 4], [7, 3], [9, 7]),
        ([3, 4], [7, 3], [0, 8]),
        ([5, 6, 8], [3], [8, 6, 8]),
        ([3], [5, 6, 8], [8, 6, 8]),
        ([5, 6, 8], [5, 6, 8, 7, 4], [0, 3, 7, 8, 4]),
        ([5, 6, 8, 7, 4], [5, 6, 8], [0, 3, 7, 8, 4]),
    ]
)
@pytest.mark.parametrize('func',
                         [sum_lists_least_significant_first,
                          sum_lists_least_significant_first_iterative])
def test_sum_lists_least_significant_first(l1, l2, expected, func):
    sum_list = func(linked_list(l1),
                    linked_list(l2))
    assert list(sum_list) == expected

# @pytest.mark.parametrize(
#     'l1,l2,expected',
#     [
#         ([1], [1], [2]),
#         ([2, 4], [7, 3], [9, 7]),
#         ([3, 4], [7, 3], [1, 0, 7]),
#         ([5, 6, 8], [3], [8, 7, 2]),
#         ([3], [5, 6, 8], [8, 7, 2]),
#         ([5, 6, 8], [5, 6, 8, 7, 4], [5, 7, 4, 4, 2]),
#         ([5, 6, 8, 7, 4], [5, 6, 8], [5, 7, 4, 4, 2]),
#     ]
# )
# def ttest_sum_lists_least_significant_last(l1, l2, expected):
#     sum_list = sum_lists_least_significant_last(linked_list(l1),
#                                                 linked_list(l2))
#     assert list(sum_list) == expected
