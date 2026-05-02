# Doubly Linked List in Python

## Overview
This project implements a **Doubly Linked List (DLL)** in Python.  
Each node in the list contains:
- A value (`value`)
- A pointer to the next node (`next`)
- A pointer to the previous node (`prev`)

The list supports basic operations such as appending elements and traversing both forward and backward.

---

## Features
- Append elements to the end of the list
- Traverse the list from head to tail (forward)
- Traverse the list from tail to head (backward)
- Handles empty list cases safely

---

## Class Structure

### `Node`
Represents a single element in the list.

**Attributes:**
- `value`: The data stored in the node
- `next`: Pointer to the next node
- `prev`: Pointer to the previous node

---

### `DLinkedList`
Represents the doubly linked list.

**Attributes:**
- `head`: The first node in the list

**Methods:**

#### `append(value)`
Adds a new node to the end of the list.

#### `traverse_forward()`
Prints all elements from head to tail.

#### `traverse_backward()`
Prints all elements from tail to head.

---

## Example Usage

```python
dll = DLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()