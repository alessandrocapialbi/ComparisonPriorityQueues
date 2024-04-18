import matplotlib.pyplot as plt
import time
import random
from HeapPriorityQueue import HeapPriorityQueue
from UnsortedLinkedListPriorityQueue import UnsortedLinkedListPriorityQueue
from SortedLinkedListPriorityQueue import SortedLinkedListPriorityQueue


class PlotGenerator:

    def __init__(self):
        pass

    def measure_insertion_time(self, pq, n, timeCalculation, randomRange=10000):
        if (isinstance(pq, HeapPriorityQueue)):
            name = "Heap"
        elif (isinstance(pq, UnsortedLinkedListPriorityQueue)):
            name = "Unsorted List"
        elif (isinstance(pq, SortedLinkedListPriorityQueue)):
            name = "Sorted List"
        else:
            name = "Unknown"
        times = [0] * (n + 1)  # Initialize the list with zeros
        s = time.time()
        for i in range(0, n):
            start_time = time.perf_counter()
            pq.insert(random.randint(0, randomRange))  # Insert random values
            insertion_time = (time.perf_counter() - start_time)
            if (not timeCalculation):
                times[i + 1] = insertion_time + times[i]
            else:
                times[i + 1] = (insertion_time / pq.get_size()) + times[i]

        end_time = time.time()
        print(name + f" insertion time: {end_time - s}")
        return times

    def measure_insertion_time_2(self, pq, n, timeCalculation, randomRange=10000):
        if (isinstance(pq, HeapPriorityQueue)):
            name = "Heap"
        elif (isinstance(pq, UnsortedLinkedListPriorityQueue)):
            name = "Unsorted List"
        elif (isinstance(pq, SortedLinkedListPriorityQueue)):
            name = "Sorted List"
        else:
            name = "Unknown"
        times = [0] * (n + 1)  # Initialize the list with zeros
        s = time.time()
        for i in range(0, n):
            start_time = time.perf_counter()
            pq.insert(random.randint(0, randomRange))  # Insert random values
            insertion_time = (time.perf_counter() - start_time)
            if (not timeCalculation):
                times[i + 1] = insertion_time + times[i]
            else:
                times[i + 1] = (insertion_time / pq.get_size())

        end_time = time.time()
        print(name + f" insertion time: {end_time - s}")
        return times

    def measure_extraction_time(self, pq, n, timeCalculation):
        if (isinstance(pq, HeapPriorityQueue)):
            name = "Heap"
        elif (isinstance(pq, UnsortedLinkedListPriorityQueue)):
            name = "Unsorted List"
        elif (isinstance(pq, SortedLinkedListPriorityQueue)):
            name = "Sorted List"
        else:
            name = "Unknown"
        times = [0] * (n + 1)  # Initialize the list with zeros

        s = time.time()
        for i in range(0, n):
            start_time = time.perf_counter()
            pq.extract_max()  # Insert random values
            extraction_time = (time.perf_counter() - start_time)
            if pq.get_size() != 0:
                if (not timeCalculation):
                    times[i + 1] = extraction_time + times[i]
                else:
                    times[i + 1] = (extraction_time / pq.get_size()) + times[i]
            else:
                times[i + 1] = 0

        end_time = time.time()
        print(f"n = {n} " + name + f" extraction time: {end_time - s}")

        return times

    def measure_extraction_time_2(self, pq, n, timeCalculation):
        if (isinstance(pq, HeapPriorityQueue)):
            name = "Priority Queue"
        elif (isinstance(pq, UnsortedLinkedListPriorityQueue)):
            name = "Unsorted List"
        elif (isinstance(pq, SortedLinkedListPriorityQueue)):
            name = "Sorted List"
        else:
            name = "Unknown"
        times = [0] * (n + 1)  # Initialize the list with zeros

        s = time.time()
        for i in range(0, n):
            start_time = time.perf_counter()
            pq.extract_max()  # Extract max value
            extraction_time = (time.perf_counter() - start_time)
            if (not timeCalculation):
                times[i + 1] = extraction_time + times[i]
            else:
                times[i + 1] = (extraction_time / (i + 1)) + times[i]

        end_time = time.time()
        print(f"\nn = {n} " + name + f" extraction time: {end_time - s}")

        return times

    def measure_extraction_time_3(self, pq, n):
        if (isinstance(pq, HeapPriorityQueue)):
            name = "Priority Queue"
        elif (isinstance(pq, UnsortedLinkedListPriorityQueue)):
            name = "Unsorted List"
        elif (isinstance(pq, SortedLinkedListPriorityQueue)):
            name = "Sorted List"
        else:
            name = "Unknown"
        times = [0] * (n + 1)  # Initialize the list with zeros
        moving_averages = [0] * (n + 1)  # Initialize the list with zeros
        s = time.time()
        for i in range(0, n):
            start_time = time.perf_counter()
            pq.extract_max()  # Extract max value
            extraction_time = (time.perf_counter() - start_time)
            if (pq.get_size() != 0):
                times[i + 1] = (extraction_time / pq.get_size())
            else:
                times[i + 1] = extraction_time

        end_time = time.time()
        print(f"\nn = {n} " + name + f" extraction time: {end_time - s}")
        return times

    def plot(self, times, n, label, color):
        plt.figure(figsize=(12, 8))
        plt.plot(range(0, n), times[1:], marker='o', label=label, color=color, linestyle='dotted', linewidth=0.2, )
        plt.xlabel('Number of operations')
        plt.ylabel('Time (s)')
        if label == 'Heap Insertion' or label == 'Sorted List Insertion' or label == 'Unsorted List Insertion':
            plt.title('Insertion Time vs Number of elements')
        else:
            plt.title('Extraction Time vs Number of elements')
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.legend()
        plt.savefig(f'{label}.png')  # Save the figure
        plt.show()

    def compare_plots(self, data, n, title, colors):
        plt.figure(figsize=(12, 8))
        for (times, label), color in zip(data, colors):
            plt.plot(range(0, n), times[1:], marker='o', label=label, color=color, linestyle='dotted', linewidth=0.2)
        plt.xlabel('Number of operations')
        plt.ylabel('Time (s)')
        plt.title(title)
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.legend()
        plt.savefig(f'{title}.png')  # Save the figure
        plt.show()
