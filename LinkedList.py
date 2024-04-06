from abc import ABC, abstractmethod


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @abstractmethod
    def insert(self, key):
        pass

    @abstractmethod
    def extract_max(self):
        pass

    def get_head(self):
        return self.head

    def set_head(self, head):
        self.head = head

    def get_tail(self):
        return self.tail

    def set_tail(self, tail):
        self.tail = tail
