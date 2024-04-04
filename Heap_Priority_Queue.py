from Heap_Queue_Node import HeapQueueNode


class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def insert(self, key):
        self.heap_size += 1
        new_node = HeapQueueNode(key)
        new_node.key = float('-inf')
        self.heap.append(new_node)
        self.heap_increase_key(self.heap_size - 1, key)

    def heap_increase_key(self, i, key):
        if key < self.heap[i].key:
            raise ValueError('New key is smaller than current key')
        self.heap[i].key = key
        while i > 0 and self.heap[self.parent(i)].key < self.heap[i].key:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def parent(self, i):
        return (i - 1) // 2

    def _max_heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[index]:
            max = left_child
        else:
            max = index

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[max]:
            max = right_child

        if max != index:
            self.heap[index], self.heap[max] = self.heap[max], self.heap[index]
            self._max_heapify(max)

    def extract_max(self):
        if len(self.heap) < 1:
            raise ValueError("Heap underflow")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._max_heapify(0)
        return max_val
