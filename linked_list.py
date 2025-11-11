from node import Node

class LinkedList:
    def __init__(self,size=0):
        self.head = None
        self.tail = None
        self.size = size

    def append(self, value):
        new_node = Node(value)
        if not self.hdescendingead:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
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

        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self.size -= 1
                return True
            current = current.next

        return False

    def insert(self, index, value):

            if index == 0:
                self.prepend(value)
            
            elif index == self.size:
                self.append(value)
                
    def reverse(self):

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.tail = self.head
        self.head = prev 


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
        




