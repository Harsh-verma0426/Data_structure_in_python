# Data_structure_in_python

A collection of **core data structures** implemented in **Python**, starting with a custom-built **Linked List**.  
This repository is designed for learning, practice, and strengthening your foundation in **Data Structures & Algorithms (DSA)**.

---

## 📂 Project: Linked List Implementation

### 📋 Overview
This module demonstrates how a **singly linked list** works — a fundamental linear data structure that stores elements as connected nodes.

Each node contains:
- **value** → The data it holds  
- **next** → A pointer to the next node in the list

The `LinkedList` class provides a clean interface for basic operations such as insertion, deletion, traversal, and searching.

---

## 🧩 Classes

### 🧱 `Node`
Represents one node in the linked list.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

🔗 LinkedList
Handles all the linked list operations and keeps track of the head, tail, and size.

⚙️ Features
✅ Append elements to the end
✅ Prepend elements to the beginning
✅ Insert at a specific index
✅ Delete a node by value
✅ Search for a value in the list
✅ Display all elements
✅ Get current size of the list

💻 Example Usage
python
Copy code
from linked_list import LinkedList

# Create a new LinkedList
ll = LinkedList()

# Add elements
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert(1, 15)

# Display the list
ll.display()   # Output: [5, 15, 10, 20]

# Search for a value
print(ll.search(10))  # True

# Delete a node
ll.delete(15)
ll.display()   # Output: [5, 10, 20]

# Get the size
print("Size:", ll.get_size())  # 3
🧮 Methods Summary
Method	Description
append(value)	Add a node at the end
prepend(value)	Add a node at the beginning
insert(index, value)	Insert a node at a specific index
delete(value)	Delete the first node matching the value
search(value)	Check if a value exists
display()	Print all elements
get_size()	Return the number of nodes
```
🧰 Tech Stack
Language: Python 3

Paradigm: Object-Oriented Programming

Focus: Data Structures, Algorithm Design

🚀 Future Additions
This repository will grow to include:

Doubly Linked List

Stack (using Linked List & Array)

Queue

Binary Search Tree (BST)

Graphs

Hash Tables


🌟 Contributing
Contributions are welcome!
If you’d like to improve the code or add new data structures, feel free to:

Fork this repository

Create a feature branch

Commit your changes

Open a pull request 🚀

🏷️ Repository
Repository Name: Data_structure_in_python
📁 A growing collection of core data structures implemented cleanly and from scratch.
