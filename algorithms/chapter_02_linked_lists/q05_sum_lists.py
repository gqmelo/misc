from algorithms.chapter_02_linked_lists.common import Node


def sum_lists_least_significant_first(l1, l2):
    return do_sum_lists(l1, l2, 0)


def do_sum_lists(l1, l2, carry):
    if not l1 and not l2 and carry == 0:
        return None

    sum = carry
    if l1:
        sum += l1.data
    if l2:
        sum += l2.data
    node = Node(sum % 10)
    node.next = do_sum_lists(l1.next if l1 else None,
                             l2.next if l2 else None,
                             sum // 10)
    return node


def sum_lists_least_significant_first_iterative(l1, l2):
    if not l1 and not l2:
        return None

    tail = None
    head = None
    carry = 0
    while l1 or l2:
        d1 = 0
        d2 = 0
        if l1:
            d1 = l1.data
        if l2:
            d2 = l2.data
        sum = d1 + d2 + carry
        node = Node(sum % 10)
        if head is None:
            head = node
            tail = head
        else:
            tail.next = node
            tail = tail.next
        carry = sum // 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return head
