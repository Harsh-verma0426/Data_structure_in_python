from stack.stack import Stack

s = Stack()

s.push(10)
s.push(20)
s.push(30)  
print("Stack after pushes:", s)
print("Top element is:", s.peek())
s.pop()
print(s)