class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next
