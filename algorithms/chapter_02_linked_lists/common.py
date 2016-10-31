
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node.data
            node = node.next

    def __repr__(self):
        return str(self.data)
