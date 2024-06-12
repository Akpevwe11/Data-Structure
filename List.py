class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """Return the data stored in the node"""
        return self.data

    def set_data(self, data):
        """Set the data stored in the node"""
        self.data = data

    def get_next(self):
        """Return the next node"""
        return self.next

    def set_next(self, new_next):
        """Set the next node"""
        self.next = new_next

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
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

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
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
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(4)
    linkedlist.append(5)
    print("Initial list:", linkedlist)
