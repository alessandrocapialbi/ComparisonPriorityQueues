import matplotlib.pyplot as plt
import time
from HeapPriorityQueue import HeapPriorityQueue
from LinkedListPriorityQueue import LinkedListPriorityQueue
from SortedLinkedListPriorityQueue import SortedLinkedListPriorityQueue
import numpy as np
import random


class PlotGenerator:

    def __init__(self):
        self.operations_heap = []
        self.operations_unsorted_list = []
        self.operations_sorted_list = []

    def measure_insertion_time(self, pq, num_elements, randomRange=5000):
        times = [0] * (num_elements + 1)  # Initialize the list with zeros
        s = time.time()
        for i in range(0, num_elements):
            start_time = time.perf_counter()
            pq.insert(random.randint(0, randomRange))  # Insert random values
            insertion_time = (time.perf_counter() - start_time)
            times[i + 1] = (insertion_time / pq.get_size()) + times[i]

        end_time = time.time()
        print(f"Elapsed time: {end_time - s}")
        return times

    def plot_insertion_time(self, times, num_elements, label):
        plt.figure(figsize=(12, 8))
        plt.plot(range(0, num_elements), times[1:], marker='o', linestyle='dotted', label=label)
        plt.xlabel('Number of operations')
        plt.ylabel('Time (s)')
        plt.title('Insertion Time vs Number of elements')
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.legend()
        plt.show()
