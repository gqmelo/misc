
def remove_dups(node):
    current = node
    runner = current
    while current is not None:
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
        runner = current
    return node
