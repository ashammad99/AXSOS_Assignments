# Singly Linked List in Python

## Overview
This project implements a **Singly Linked List** in Python using two classes:

- `Node`: Represents a single node in the list.
- `SLinkedList`: Represents the linked list and provides methods to add, remove, print, and insert values.

This implementation is useful for understanding the basic operations of linked lists and how nodes are connected in memory.

---

## Classes

### `Node`
A node stores:
- `value`: the data inside the node
- `next`: a reference to the next node

### `SLinkedList`
The linked list stores:
- `head`: the first node in the list

---

## Methods

### `add_to_front(value)`
Adds a new node to the beginning of the list.

**Parameters:**
- `value`: value to insert

**Returns:**
- `self`

---

### `printValues()`
Prints all node values from the head to the end.

**Returns:**
- `self`

---

### `add_to_back(value)`
Adds a new node to the end of the list.

**Parameters:**
- `value`: value to insert

**Returns:**
- `self`

---

### `remove_from_front()`
Removes the first node from the list.

**Returns:**
- The removed value, or `None` if the list is empty

---

### `remove_from_back()`
Removes the last node from the list.

**Returns:**
- The removed value, or `None` if the list is empty

---

### `removeVal(value)`
Removes the first node that contains the given value.

**Parameters:**
- `value`: value to remove

**Returns:**
- `True` if the value was found and removed
- `False` otherwise

---

### `insertAt(value, n)`
Inserts a new node at index `n`.

**Parameters:**
- `value`: value to insert
- `n`: target index

**Returns:**
- `self`

**Behavior:**
- If `n == 0`, the value is inserted at the front
- If `n` is greater than the list length, the value is added at the back

---

## Example Usage

```python
lst = SLinkedList()

lst.add_to_front(3).add_to_front(2).add_to_front(1)
lst.add_to_back(4).add_to_back(5)
lst.printValues()

print("Removed from front:", lst.remove_from_front())
print("Removed from back:", lst.remove_from_back())

lst.removeVal(3)
lst.insertAt(10, 1)
lst.printValues()