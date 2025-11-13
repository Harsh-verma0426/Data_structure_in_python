# 🧠 Data Structure in Python

A collection of **core data structures** implemented in **Python**, including **Singly**, **Doubly**, and now **Circular** Linked Lists.  
This repository is designed for learning, practicing, and strengthening your foundation in **Data Structures & Algorithms (DSA)**.

---

## 📂 Package Structure

The `linked_list` folder acts as a package, allowing clean imports like:

```python
from linked_list.linked_list import LinkedList
from linked_list.doubly_linked_list import DoublyLinkedList
from linked_list.circular_linked_list import CircularLinkedList
```
🧩 Classes
🧱 Node
Represents one node in a linked list.
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None   # used only in Doubly Linked List
```
🔗 Singly Linked List
⚙️ Features

✅ Append elements

✅ Prepend elements

✅ Insert at specific index

✅ Delete by value

✅ Search

✅ Reverse

✅ Sort (ascending/descending)

✅ max() / min()

✅ Iterable (__iter__)

✅ Printable (__str__)

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
append(value)	Add a node at the end
prepend(value)	Add at the beginning
insert(index, value)	Insert at specific position
delete(value)	Delete by value
reverse()	Reverse the list
sort(descending=False)	Sort the list
max() / min()	Largest / smallest value
search(value)	Check if value exists
__iter__()	Make iterable
__str__()	Display as [1, 2, 3]
```
🔁 Doubly Linked List
⚙️ Features
✅ Append (bidirectional update)

✅ Prepend

✅ Insert at index

✅ Delete by value

✅ Search

✅ Forward traversal

✅ Backward traversal

✅ Sort, Max, Min

✅ Iterable + Printable

💻 Example Usage
```
from linked_list.doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)

print("Doubly:", dll)       # [5, 10, 20]
dll.delete(10)
print("After delete:", dll) # [5, 20]

for value in dll:
    print(value)
```
🧮 Methods Summary
Method	Description
```
append(value)	Add at end
prepend(value)	Add at beginning
insert(index, value)	Insert at index
delete(value)	Delete by value
search(value)	Contains value?
sort(descending=False)	Sort list
max() / min()	Largest / smallest
__iter__()	Iterate
__str__()	Print as [5, 10, 20]
```

🔄 Circular Linked List
⚙️ Features
✅ Append (maintains circular structure)

✅ Prepend

✅ Delete by value (including head & tail handling)

✅ Search

✅ Fully circular iteration

✅ Printable using __str__()

✅ Zero edge-case bugs (head, tail, 1-node list)

💻 Example Usage
```
from linked_list.circular_linked_list import CircularLinkedList

cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.prepend(5)

print("Circular:", cll)      # [5, 10, 20]

cll.delete(10)
print("After delete:", cll)  # [5, 20]

for val in cll:
    print(val)
🧮 Methods Summary
Method	Description
append(value)	Add to the end (circular)
prepend(value)	Add to the start
delete(value)	Delete by value
search(value)	Search entire circular loop
__iter__()	Iterate full circle safely
__str__()	Print as [a, b, c]
```
🧰 Tech Stack
Language: Python 3

Paradigm: Object-Oriented Programming

Focus: Data Structures & Algorithms

🚀 Future Additions
Stack (LL + Array version)

Queue

Binary Search Tree (BST)

Graphs

Hash Tables

🌟 Contributing
Contributions are welcome!
Steps to contribute:

Fork the repo

Create a feature branch

Commit your changes

Open a pull request 🚀

🏷️ Repository Info
Repository: data_structure_in_python
📁 A growing collection of clean, from-scratch implementations of fundamental data structures.
