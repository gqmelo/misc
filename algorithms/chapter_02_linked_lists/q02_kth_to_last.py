
def get_kth_to_last(node, k):
    last = node
    kth = node
    for i in range(k - 1):
        if last.next is None:
            return None
        last = last.next
    while last.next is not None:
        last = last.next
        kth = kth.next
    return kth


def get_kth_to_last_recursive(node, k):
    result, i = do_get_kth_to_last(node, k)
    return result


def do_get_kth_to_last(head, k):
    if head is None:
        return None, 0

    node, i = do_get_kth_to_last(head.next, k)
    i += 1
    if i == k:
        return head, i
    else:
        return node, i

