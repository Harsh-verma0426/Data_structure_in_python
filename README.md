# 🧠 Data Structure in Python

A collection of **core data structures** implemented in **Python**, starting with custom-built **Linked Lists** — both **Singly** and **Doubly** linked lists.  
This repository is designed for learning, practicing, and strengthening your foundation in **Data Structures & Algorithms (DSA)**.

---

## 📂 Projects Included

### 1️⃣ Singly Linked List  
A basic implementation of a linear linked list where each node contains:
- **value** → The data it holds  
- **next** → A pointer to the next node in the list  

### 2️⃣ Doubly Linked List  
An enhanced version where each node has two pointers:
- **value** → The data it holds  
- **next** → A pointer to the next node  
- **prev** → A pointer to the previous node  

This makes **bidirectional traversal** and certain operations (like deletion) much easier and more efficient.

---

## 🧩 Classes

### 🧱 Node (for both lists)

class Node:
def init(self, value):
self.value = value
self.next = None
# for doubly linked list
self.prev = None

yaml
Copy code

---

## ⚙️ Singly Linked List — Features

- ✅ Append elements to the end  
- ✅ Prepend elements to the beginning  
- ✅ Insert at a specific index  
- ✅ Delete a node by value  
- ✅ Search for a value  
- ✅ Display all elements  
- ✅ Get list size  
- ✅ Find max and min values  
- ✅ Sort the list (ascending or descending)

---

### 💻 Example Usage (Singly Linked List)

from linked_list import LinkedList

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert(1, 15)

ll.display() # [5, 15, 10, 20]
print(ll.search(10)) # True

ll.delete(15)
ll.display() # [5, 10, 20]

print("Max:", ll.max()) # 20
print("Min:", ll.min()) # 5

ll.sort() # Ascending
ll.display() # [5, 10, 20]

ll.sort(descending=True) # Descending
ll.display() # [20, 10, 5]

yaml
Copy code

---

## 🧮 Singly Linked List — Methods Summary

| Method | Description |
|--------|--------------|
| `append(value)` | Add a node at the end |
| `prepend(value)` | Add a node at the beginning |
| `insert(index, value)` | Insert at a specific position |
| `delete(value)` | Delete a node with given value |
| `search(value)` | Check if a value exists |
| `display()` | Print all elements |
| `get_size()` | Return list size |
| `max()` | Return the maximum value |
| `min()` | Return the minimum value |
| `sort(descending=False)` | Sort the list |

---

## 🔗 Doubly Linked List — Features

- ✅ Append elements (updates both next and prev links)  
- ✅ Prepend elements (adds node at the beginning)  
- ✅ Delete node by value (handles both directions)  
- ✅ Search for a value  
- ✅ Forward traversal (`display()`)  
- ✅ Backward traversal (`display_reverse()`)  
- ✅ Maintain size dynamically  

---

### 💻 Example Usage (Doubly Linked List)

from doubly_linked_list import Doubly_linkedList

dll = Doubly_linkedList()

dll.append(10)
dll.append(20)
dll.prepend(5)

dll.display() # [5, 10, 20]
dll.display_reverse() # [20, 10, 5]

dll.delete(10)
dll.display() # [5, 20]

print("Size:", dll.get_size()) # 2
print(dll.search(20)) # True

yaml
Copy code

---

## 🧮 Doubly Linked List — Methods Summary

| Method | Description |
|--------|--------------|
| `append(value)` | Add a node at the end |
| `prepend(value)` | Add a node at the beginning |
| `delete(value)` | Delete node (updates both directions) |
| `search(value)` | Search by value |
| `display()` | Display list forward |
| `display_reverse()` | Display list backward |
| `get_size()` | Return total number of nodes |

---

## 🧰 Tech Stack

- **Language:** Python 3  
- **Paradigm:** Object-Oriented Programming  
- **Focus:** Data Structures, Algorithm Design  

---

## 🚀 Future Additions

This repository will soon include:
- Doubly Linked List (completed ✅)  
- Stack (using Linked List)  
- Queue  
- Binary Search Tree (BST)  
- Graphs  
- Hash Tables  

---

## 🌟 Contributing

Contributions are welcome!  
If you’d like to improve the code or add new data structures, feel free to:

1. **Fork** this repository  
2. **Create** a feature branch  
3. **Commit** your changes  
4. **Open** a pull request 🚀  

---

## 🏷️ Repository Info

**Repository Name:** `data_structure_in_python`  
📁 A growing collection of clean, from-scratch implementations of core data structures.
