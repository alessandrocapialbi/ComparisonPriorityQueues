from Node import Node


class LinkedListPriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        new_node = Node(key)
        if not self.head:  # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def extract_max(self):
        if not self.head:
            return None
        max_value = self.head.key
        current = self.head.next
        while current:
            if current.key > max_value:
                max_value = current.key
            current = current.next
        return max_value
