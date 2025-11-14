from nodes.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return str(values)