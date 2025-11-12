from nodes.doubly_node import Node

class Doubly_linkedList:
    def __init__(self,size=0):
        self.head = None
        self.tail = None
        self.size = size

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)

    def get_size(self):
        return self.size
    
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def delete(self, value):
        if self.head is None:
            return False

        current = self.head

        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True
            current = current.next
        return False