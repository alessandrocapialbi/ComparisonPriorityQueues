from Node import Node
from LinkedList import LinkedList


class LinkedListPriorityQueue(LinkedList):

    def insert(self, key):
        node = Node(key)
        if not self.head:  # If list is empty
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def extract_max(self):
        if not self.head:
            return None
        max_value = self.head.key
        current = self.head.get_next()
        while current:
            if current.key > max_value:
                max_value = current.key
            current = current.get_next()
        return max_value

