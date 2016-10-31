
def partition(head, value):
    if head is None or head.next is None:
        return head
    node = head
    next_node = node.next
    while next_node is not None:
        if next_node.data < value:
            node.next = next_node.next
            next_node.next = head
            head = next_node
        else:
            node = node.next
        next_node = node.next

    return head


def partition_book(node, x):
    head = node
    tail = node

    while node is not None:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None

    return head
