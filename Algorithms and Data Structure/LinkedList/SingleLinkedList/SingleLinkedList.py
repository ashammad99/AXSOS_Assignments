class Node:
    # Represents a single node in the singly linked list
    def __init__(self, value):
        self.next = None      # Reference to the next node
        self.value = value    # Value stored in the node


class SLinkedList:
    # Represents a singly linked list
    def __init__(self):
        self.head = None  # First node in the list

    def add_to_front(self, value):
        """
        Add a new node to the beginning of the list.

        Args:
            value: The value to store in the new node.

        Returns:
            SLinkedList: Returns self to allow method chaining.
        """
        new_node = Node(value)      # Create a new node
        new_node.next = self.head   # Point new node to current head
        self.head = new_node        # Update head to the new node
        return self

    def printValues(self):
        """
        Print all values in the linked list from head to tail.

        Returns:
            SLinkedList: Returns self to allow method chaining.
        """
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, value):
        """
        Add a new node to the end of the list.

        Args:
            value: The value to store in the new node.

        Returns:
            SLinkedList: Returns self to allow method chaining.
        """
        # If the list is empty, add directly to the front
        if self.head is None:
            return self.add_to_front(value)

        new_node = Node(value)
        runner = self.head

        # Traverse until the last node
        while runner.next is not None:
            runner = runner.next

        # Set the last node's next reference to the new node
        runner.next = new_node
        return self

    def remove_from_front(self):
        """
        Remove and return the value of the first node.

        Returns:
            The removed value if the list is not empty, otherwise None.
        """
        if self.head is None:
            return None

        value = self.head.value     # Store the head value
        self.head = self.head.next  # Move head to the next node
        return value

    def remove_from_back(self):
        """
        Remove and return the value of the last node.

        Returns:
            The removed value if the list is not empty, otherwise None.
        """
        if self.head is None:
            return None

        # If there is only one node
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value

        runner = self.head

        # Stop at the second-to-last node
        while runner.next.next is not None:
            runner = runner.next

        value = runner.next.value   # Save the last node's value
        runner.next = None          # Remove the last node
        return value

    def removeVal(self, value):
        """
        Remove the first node that contains the given value.

        Args:
            value: The value to remove.

        Returns:
            bool: True if a node was removed, otherwise False.
        """
        if self.head is None:
            return False

        # If the head contains the target value
        if self.head.value == value:
            self.head = self.head.next
            return True

        runner = self.head

        # Search for the node before the target node
        while runner.next is not None:
            if runner.next.value == value:
                runner.next = runner.next.next  # Skip the target node
                return True
            runner = runner.next

        return False

    def insertAt(self, value, n):
        """
        Insert a new node at index n.

        Args:
            value: The value to insert.
            n (int): The target index.

        Returns:
            SLinkedList: Returns self to allow method chaining.

        Notes:
            - If n == 0, the value is inserted at the front.
            - If n is greater than the list length, the value is added at the back.
        """
        if n == 0:
            return self.add_to_front(value)

        new_node = Node(value)
        runner = self.head
        index = 0

        # Traverse to the node before the target index
        while runner is not None and index < n - 1:
            runner = runner.next
            index += 1

        # If index is out of range, add to the back
        if runner is None:
            return self.add_to_back(value)

        # Insert the new node in the correct position
        new_node.next = runner.next
        runner.next = new_node

        return self


print("=== Start Testing ===")

lst = SLinkedList()

print("\n1) Empty list:")
lst.printValues()

print("\n2) Add to front:")
lst.add_to_front(3).add_to_front(2).add_to_front(1)
lst.printValues()   # Expected: 1, 2, 3

print("\n3) Add to back:")
lst.add_to_back(4).add_to_back(5)
lst.printValues()   # Expected: 1, 2, 3, 4, 5

print("\n4) Remove from front:")
print("Removed:", lst.remove_from_front())
lst.printValues()   # Expected: 2, 3, 4, 5

print("\n5) Remove from back:")
print("Removed:", lst.remove_from_back())
lst.printValues()   # Expected: 2, 3, 4

print("\n6) Remove value (3):")
lst.removeVal(3)
lst.printValues()   # Expected: 2, 4

print("\n7) Remove value (2):")
lst.removeVal(2)
lst.printValues()   # Expected: 4

print("\n8) Remove value (4):")
lst.removeVal(4)
lst.printValues()   # Expected: Empty list

print("\n9) Insert at positions:")
lst.insertAt(10, 0)   # Insert at front
lst.insertAt(30, 1)   # Insert at end
lst.insertAt(20, 1)   # Insert in middle
lst.printValues()     # Expected: 10, 20, 30

print("\n10) Insert beyond length:")
lst.insertAt(40, 10)
lst.printValues()     # Expected: 10, 20, 30, 40

print("\n11) Remove from single-node list:")
single = SLinkedList()
single.add_to_front(99)
single.printValues()
print("Removed:", single.remove_from_back())
single.printValues()