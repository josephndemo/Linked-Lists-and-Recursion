class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        - Create a new Node with 'data'.
        - Insert it at the front of the list.
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        - Use recursion to sum all node data in the list.
        """
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        - Reverse the list in-place using recursion.
        """
        def helper(prev, current):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        - Return True if 'target' is found, otherwise False.
        """
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        - Print the contents of the list.
        """
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        values.append("None")
        print(" -> ".join(values))