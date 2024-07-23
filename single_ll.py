class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Insert
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

# Delete
    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                return True
            prev = current
            current = current.next
        return False

# Traverse
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Testing the implementation
my_ll = SinglyLinkedList()
my_ll.append("a")
my_ll.append("b")
my_ll.append("c")
my_ll.traverse()  # Output: 1 -> 2 -> 3 -> None
my_ll.delete("b")
my_ll.traverse()  # Output: 1 -> 3 -> None
