# 🧠 Data Structure in Python

A collection of **core data structures** implemented in **Python**, including:

- Singly Linked List  
- Doubly Linked List  
- Circular Linked List  
- Stack (LinkedList-based)

This project is designed for learning, practicing, and strengthening your foundation in **Data Structures & Algorithms (DSA)**.

---

## 📂 Package Structure

data_structure_in_python/
│
├── linked_list/
│ ├── linked_list.py
│ ├── doubly_linked_list.py
│ └── circular_linked_list.py
│
└── stack/
└── stack.py

python
Copy code

Import examples:

```python
from linked_list.linked_list import LinkedList
from linked_list.doubly_linked_list import DoublyLinkedList
from linked_list.circular_linked_list import CircularLinkedList
from stack.stack import Stack
```
🧩 Classes
🧱 Node
Used internally by all linked list structures.

```    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # used only in Doubly Linked List
```
🔗 Singly Linked List
⚙️ Features
Append

Prepend

Insert at index

Delete

Search

Reverse

Sort

Max / Min

Iterable

Printable

💻 Example Usage
```
from linked_list.linked_list import LinkedList

ll = LinkedList()
ll.append(10)
ll.prepend(5)
ll.append(20)

print("Singly:", ll)         # [5, 10, 20]
print("Max:", ll.max())      # 20

ll.reverse()
print("Reversed:", ll)       # [20, 10, 5]
```
🧮 Methods Summary
Method	Description
```
append(value)	Add at end
prepend(value)	Add at beginning
insert(index, value)	Insert node
delete(value)	Delete by value
reverse()	Reverse list
sort(descending=False)	Sort
max() / min()	Largest / smallest
search(value)	Find element
__iter__()	Iterate through list
__str__()	Print as [1, 2, 3]
```

🔁 Doubly Linked List
⚙️ Features
Append & Prepend

Insert at index

Delete

Search

Forward & backward traversal

Max / Min

Sort

Iterable

Printable

💻 Example Usage
```
from linked_list.doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)

print("Doubly:", dll)        # [5, 10, 20]
dll.delete(10)
print("After delete:", dll)  # [5, 20]

for value in dll:
    print(value)
```
🧮 Methods Summary
Method	Description
```
append(value)	Add at end
prepend(value)	Add at start
insert(index, value)	Insert
delete(value)	Delete node
search(value)	Check if exists
sort(descending=False)	Sort list
max() / min()	Largest / smallest
__iter__()	Iterate
__str__()	Print clean list
```
🔄 Circular Linked List
⚙️ Features
Append

Prepend

Delete (head, tail, middle)

Search

Full circular traversal

Iterable

Printable

Zero edge-case failures

💻 Example Usage
```
from linked_list.circular_linked_list import CircularLinkedList

cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.prepend(5)

print("Circular:", cll)       # [5, 10, 20]

cll.delete(10)
print("After delete:", cll)   # [5, 20]

for val in cll:
    print(val)
```
🧮 Methods Summary
Method	Description
```
append(value)	Add to end (circular)
prepend(value)	Add at start
delete(value)	Safe deletion
search(value)	Full circle search
__iter__()	Circular iteration
__str__()	Print as [a, b, c]
```
📦 Stack (Linked List Based)
A classic LIFO stack implemented using the same Node structure as LinkedList.

⚙️ Features
Push

Pop

Peek

is_empty

Length

Printable

O(1) operations

💻 Example Usage
```
from stack.stack import Stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack:", s)          # [30, 20, 10]
print("Top:", s.peek())     # 30

print("Popped:", s.pop())   # 30
print("After pop:", s)      # [20, 10]
```
🧮 Methods Summary
Method	Description
```
push(value)	Add element to top
pop()	Remove and return top
peek()	View top
is_empty()	Stack empty?
__len__()	Size
__str__()	Print stack
```
🧰 Tech Stack
Language: Python 3

Paradigm: Object-Oriented Programming

Focus: Data Structures & Algorithms

🚀 Future Additions
Queue

Binary Search Tree (BST)

Graphs

Hash Tables

Heap / Priority Queue

🌟 Contributing
Contributions are welcome!
Steps to contribute:

Fork the repo

Create a feature branch

Commit changes

Open a pull request 🚀

🏷️ Repository Info
Repository: data_structure_in_python
📁 A growing collection of clean, from-scratch implementations of fundamental data structures.
