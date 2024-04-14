class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get_size(self):
        return self.heap_size

    def insert(self, key):
        self.heap_size += 1
        self.heap.append(float('-inf'))
        self.heap_increase_key(self.heap_size - 1, key)

    def heap_increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError('New key is smaller than current key')
        self.heap[i] = key
        parent = self.parent(i)
        while i > 0 and self.heap[parent] < self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = self.parent(i)

    def max_heapify(self, i):
        left_child = self.left(i)
        right_child = self.right(i)
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[i]:
            max = left_child
        else:
            max = i

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[max]:
            max = right_child
        if max != i:
            self.heap[i], self.heap[max] = self.heap[max], self.heap[i]
            self.max_heapify(max)

    def extract_max(self):
        if len(self.heap) < 1:
            raise ValueError("Heap underflow")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap_size -= 1
        del self.heap[-1]
        self.max_heapify(0)
        return max_val
