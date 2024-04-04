class HeapQueueNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __gt__(self, other):
        if isinstance(other, HeapQueueNode):
            return self.key > other.key
        return NotImplemented
