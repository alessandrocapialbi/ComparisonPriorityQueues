from Node import Node


class SortedLinkedListPriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        new_node = Node(key)
        if not self.head:  # If list is empty
            self.head = new_node
            self.tail = new_node
        elif key < self.head.key:  # If the new node has a smaller key than the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.key < key:  # Find the right position for the new node
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if not new_node.next:  # If the new node is the last node
                self.tail = new_node

    def extract_max(self):
        if not self.tail:
            return None
        return self.tail.key
