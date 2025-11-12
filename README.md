# 🧠 Data Structure in Python

A collection of **core data structures** implemented in **Python**, starting with custom-built **Linked Lists** — both **Singly** and **Doubly** linked lists.  
This repository is designed for learning, practicing, and strengthening your foundation in **Data Structures & Algorithms (DSA)**.

---


The `linked_list` folder acts as a **package**, allowing clean imports like:
```python
from linked_list.linked_list import LinkedList
from linked_list.doubly_linked_list import DoublyLinkedList
```
📋 Overview
This repository demonstrates how both singly and doubly linked lists work —
two fundamental linear data structures that store data in connected nodes.

🧩 Classes
🧱 Node
Represents one node in a linked list.
```

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # only used in Doubly Linked List
```
🔗 Singly Linked List
⚙️ Features
✅ Append elements to the end

✅ Prepend elements to the beginning

✅ Insert at a specific index

✅ Delete a node by value

✅ Search for a value

✅ Reverse the list

✅ Sort (ascending or descending)

✅ Find maximum and minimum values

✅ Iterable and printable using Python magic methods (__iter__, __str__)

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
🧮 Methods Summary
Method	Description
append(value)	Add a node at the end
prepend(value)	Add a node at the beginning
insert(index, value)	Insert at a specific index
delete(value)	Delete a node by value
reverse()	Reverse the list
sort(descending=False)	Sort the list
max() / min()	Find largest/smallest value
search(value)	Check if a value exists
__iter__()	Make the list iterable
__str__()	Print as [1, 2, 3]
```

🔁 Doubly Linked List
⚙️ Features
✅ Append elements (updates both directions)

✅ Prepend elements

✅ Insert at a specific index

✅ Delete nodes by value

✅ Search for elements

✅ Forward & backward traversal

✅ Sort, Max, Min

✅ Fully iterable and printable like a Python list

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
🧮 Methods Summary
Method	Description
append(value)	Add node to the end
prepend(value)	Add node to the start
insert(index, value)	Insert at specific index
delete(value)	Delete a node by value
search(value)	Check if a value exists
sort(descending=False)	Sort the list
max() / min()	Find largest/smallest value
__iter__()	Iterate through list
__str__()	Print as [5, 10, 20]
```
🧰 Tech Stack
Language: Python 3

Paradigm: Object-Oriented Programming

Focus: Data Structures, Algorithm Design

🚀 Future Additions
This repository will grow to include:

Stack (Linked List & Array based)

Queue

Binary Search Tree (BST)

Graphs

Hash Tables

🌟 Contributing
Contributions are welcome!
If you’d like to improve the code or add new data structures:

Fork this repository

Create a feature branch

Commit your changes

Open a pull request 🚀

🏷️ Repository Info
Repository Name: data_structure_in_python
📁 A growing collection of clean, from-scratch implementations of core data structures.
