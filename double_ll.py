class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Insertion on head/tail
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Delete
    def delete_node(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev

# Traverse forward/backward
    def traverse(self, direction="forward"):
        if direction == "forward":
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
        elif direction == "backward":
            current = self.tail
            while current:
                print(current.data, end=" <-> ")
                current = current.prev
        print("None")

# Testing the implementation
dll = DoublyLinkedList()
dll.append("a")
dll.append("b")
dll.append("c")
dll.traverse("forward")   # Output: 1 <-> 2 <-> 3 <-> None
dll.traverse("backward")  # Output: 3 <-> 2 <-> 1 <-> None
dll.delete_node("b")
dll.traverse("forward")   # Output: 1 <-> 3 <-> None
dll.traverse("backward")  # Output: 3 <-> 1 <-> None
