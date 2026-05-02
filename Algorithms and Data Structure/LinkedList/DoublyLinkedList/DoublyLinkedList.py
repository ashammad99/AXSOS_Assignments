class Node:
    def __init__(self, value):
        # Store the value of the node
        self.value = value
        # Pointer to the next node
        self.next = None
        # Pointer to the previous node
        self.prev = None


class DLinkedList:
    def __init__(self):
        # Head (start) of the linked list
        self.head = None


    def append(self, value):
        """append new node to end of list
            :Parameters:
                value: the actual value to be added
            :returns: None
        """
        # Create a new node
        new_node = Node(value)

        # If the list is empty, set new node as head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next

        # Link the new node at the end
        temp.next = new_node
        new_node.prev = temp


    def traverse_forward(self):
        """
            Forward Traversal: traverse the list from head to tail

            :arg: Nothing
            :returns: Printing the forward values of the list
        """
        # Start from the head
        temp = self.head

        # Traverse forward until the end
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next

        print("None")


    def traverse_backward(self):
        """
            Backward Traversal: traverse the list from tail to head
            :arg: Nothing
            :returns: Printing the backward values of the list
        """
        temp = self.head

        # Check if the list is empty
        if not temp:
            print("List is empty!")
            return

        # Move to the last node (tail)
        while temp.next:
            temp = temp.next

        # Traverse backward using prev pointers
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.prev

        print("None")


# Example usage
dll = DLinkedList()

# Append elements
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()