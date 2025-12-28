from l04_node import Node


class LinkedList:
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            last_node = None
            for i in self:
                last_node = i
            last_node.set_next(node)
    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

