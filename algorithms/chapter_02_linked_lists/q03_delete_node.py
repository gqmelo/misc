
def delete_node(node):
    if not node or not node.next:
        return

    node.data = node.next.data
    node.next = node.next.next
