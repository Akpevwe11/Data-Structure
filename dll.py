class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return repr(self.data)

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous = new_previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return ",".join(nodes)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        current.next.previous = current

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head.previous = new_head
        self.head = new_head

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.previous = None
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                current.next.previous = current
                return
            current = current.next

    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            current.previous = next_node
            prev_node = current
            current = next_node
        self.head = prev_node
