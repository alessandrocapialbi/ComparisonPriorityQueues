import time
import random
import matplotlib.pyplot as plt
from Heap_Priority_Queue import HeapPriorityQueue
from LinkedList_Priority_Queue import LinkedListPriorityQueue
from Sorted_LinkedList_Priority_Queue import SortedLinkedListPriorityQueue


def test_performance_insertion(priority_queue, n=20000):
    random.seed(42)
    start_time = time.time()
    for _ in range(n):
        priority_queue.insert(random.randint(0, n))
    end_time = time.time()
    return end_time - start_time


def test_performance_extraction(priority_queue, n=20000):
    random.seed(42)
    start_time = time.time()
    for _ in range(n):
        priority_queue.extract_max()
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # Test performance
    heap_queue = HeapPriorityQueue()
    linked_list_queue = LinkedListPriorityQueue()
    sorted_linked_list_queue = SortedLinkedListPriorityQueue()

    heap_insertion_time = test_performance_insertion(heap_queue)
    linked_list_insertion_time = test_performance_insertion(linked_list_queue)
    sorted_linked_list_insertion_time = test_performance_insertion(sorted_linked_list_queue)

    heap_extraction_time = test_performance_extraction(heap_queue)
    linked_list_extraction_time = test_performance_extraction(linked_list_queue)
    sorted_linked_list_extraction_time = test_performance_extraction(sorted_linked_list_queue)

    print("Heap Insertion Time:", heap_insertion_time)
    print("Linked List Insertion Time:", linked_list_insertion_time)
    print("Sorted Linked List Insertion Time:", sorted_linked_list_insertion_time)

    print("Heap Extraction Time:", heap_extraction_time)
    print("Linked List Extraction Time:", linked_list_extraction_time)
    print("Sorted Linked List Extraction Time:", sorted_linked_list_extraction_time)

    # Plotting
    labels = ['Heap', 'Linked List', 'Sorted Linked List']
    insertion_times = [heap_insertion_time, linked_list_insertion_time, sorted_linked_list_insertion_time]
    extraction_times = [heap_extraction_time, linked_list_extraction_time, sorted_linked_list_extraction_time]

    fig, axs = plt.subplots(2)
    fig.suptitle('Performance Comparison of Priority Queue Implementations')

    axs[0].bar(labels, insertion_times, color='orange')
    axs[0].set_ylabel('Insertion Time (s)')

    axs[1].bar(labels, extraction_times, color='green')
    axs[1].set_ylabel('Extraction Time (s)')

    plt.show()
