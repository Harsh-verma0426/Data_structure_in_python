from nodes.list_node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.value

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.front
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return str(values)
