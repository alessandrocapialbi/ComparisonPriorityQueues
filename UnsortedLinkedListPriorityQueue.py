from Node import Node
from LinkedList import LinkedList


class UnsortedLinkedListPriorityQueue(LinkedList):

    def insert(self, key):
        self.size += 1
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

        # Find the max node
        max_node = self.head
        current = self.head.next
        while current:
            if current.key > max_node.key:
                max_node = current
            current = current.next

        # If the max node is the head
        if self.head == max_node:
            self.head = self.head.next
        else:
            # Find the node before the max node and remove max node
            current = self.head
            while current.next != max_node:
                current = current.next
            current.next = max_node.next

        # If the max node is the tail
        if self.tail == max_node:
            self.tail = current

        self.size -= 1

        return max_node.key
