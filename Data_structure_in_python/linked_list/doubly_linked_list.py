from nodes.doubly_node import Node

class DoublyLinkedList:
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

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return
        elif index == self.size:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def display(self,reverse=False):
        if not reverse:
            current = self.head
            elements = []
            while current:
                elements.append(current.value)
                current = current.next
            print(elements)

        else:
            self.display_reverse()

    def display_reverse(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.value)
            current = current.prev
        print(elements)
    
    def __len__(self):
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
    
    def sort(self, ascending=True):

        if self.head is None:
            return

        swap = True
        while swap:
            swap = False
            current = self.head

            while current.next:
                if (ascending and current.value > current.next.value) or (not ascending and current.value < current.next.value ):
                    current.value, current.next.value = current.next.value, current.value
                    swap = True
                current = current.next

    def max(self):
        if self.head is None:
            return None

        maximum = self.head.value
        current = self.head
        while current:
            if maximum < current.value:
                maximum = current.value
            current = current.next
        return maximum
        
    def min(self):
        if self.head is None:
            return None

        minimum = self.head.value
        current = self.head
        while current:
            if minimum > current.value:
                minimum = current.value
            current = current.next
        return minimum
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return str(elements)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next