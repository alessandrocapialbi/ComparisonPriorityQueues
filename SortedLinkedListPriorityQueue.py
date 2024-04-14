from Node import Node
from LinkedList import LinkedList


class SortedLinkedListPriorityQueue(LinkedList):

    def insert(self, key):
        self.size += 1
        new_node = Node(key)
        if not self.head:  # If list is empty
            self.head = self.tail = new_node
        elif key < self.head.key:  # If the new node has a smaller key than the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.key > key:  # Find the right position for the new node
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if not new_node.next:  # If the new node is the last node
                self.tail = new_node

    def extract_max(self):
        if not self.head:
            return None

        max_key = self.head.key  # Save the key of the max node
        self.head = self.head.next  # Update the head to the next node
        self.size -= 1  # Decrease the size

        if not self.head:  # If the list is now empty
            self.tail = None  # Update the tail

        return max_key
