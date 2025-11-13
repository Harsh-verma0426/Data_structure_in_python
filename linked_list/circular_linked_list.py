from nodes.node import Node

class CircularLinkedList:
    
    def __init__(self,size=0):
        self.head = None
        self.tail = None
        self.size = size

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1


    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
            self.size += 1

    def display(self):
        elements = []
        if not self.head:
            print(elements)
            return
        current = self.head
        while True:
            elements.append(current.value)
            current = current.next
            if current == self.head:
                break
        print(elements)
            
    def __len__(self):
        return self.size
    
    def search(self, value):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    def delete(self, value):
        if self.head is None:
            return False

        current = self.head

        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.size -= 1
            return True

        while True:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return True

            current = current.next
            if current == self.head:
                break

        return False
   
    def __str__(self):
        if not self.head:
            return False
        elements = []
        current = self.head
        while True:
            elements.append(current.value)
            current = current.next
            if current == self.head:
                break
        return str(elements)
    
    def __iter__(self):
        if not self.head:
            return False
        current = self.head
        while True:
            yield current.value
            current = current.next
            if current == self.head:
                break