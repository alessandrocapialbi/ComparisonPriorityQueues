from HeapPriorityQueue import HeapPriorityQueue
from UnsortedLinkedListPriorityQueue import UnsortedLinkedListPriorityQueue
from SortedLinkedListPriorityQueue import SortedLinkedListPriorityQueue
from PlotGenerator import PlotGenerator

if __name__ == "__main__":
    # Usage
    plt = PlotGenerator()

    n = 10000  # Set desired dimensions

    pq_heap = HeapPriorityQueue()
    pq_unsorted_list = UnsortedLinkedListPriorityQueue()
    pq_sorted_list = SortedLinkedListPriorityQueue()

    insertion_pq_heap_times = plt.measure_insertion_time(pq_heap, n, True)
    plt.plot(insertion_pq_heap_times, n, 'Heap Insertion', 'red')

    extraction_pq_heap_times = plt.measure_extraction_time_2(pq_heap, n, True)
    plt.plot(extraction_pq_heap_times, n, 'Heap Extraction', 'red')

    insertion_pq_unsorted_list_times = plt.measure_insertion_time_2(pq_unsorted_list, n, True)
    plt.plot(insertion_pq_unsorted_list_times, n, 'Unsorted List Insertion', 'blue')

    extraction_pq_unsorted_list_times = plt.measure_extraction_time(pq_unsorted_list, n, True)
    plt.plot(extraction_pq_unsorted_list_times, n, 'Unsorted List Extraction', 'blue')

    insertion_pq_sorted_list_times = plt.measure_insertion_time(pq_sorted_list, n, True)
    plt.plot(insertion_pq_sorted_list_times, n, 'Sorted List Insertion', 'green')

    extraction_pq_sorted_list_times = plt.measure_extraction_time_3(pq_sorted_list, n)
    plt.plot(extraction_pq_sorted_list_times, n, 'Sorted List Extraction', 'green')

    plt.compare_plots([
        (insertion_pq_heap_times, 'Heap Insertion'),
        (insertion_pq_unsorted_list_times, 'Unsorted List Insertion'),
        (insertion_pq_sorted_list_times, 'Sorted List Insertion')
    ], n, 'Insertion Time Comparison', ['red', 'blue', 'green'])

    plt.compare_plots([
        (extraction_pq_heap_times, 'Heap Extraction'),
        (extraction_pq_unsorted_list_times, 'Unsorted List Extraction'),
        (extraction_pq_sorted_list_times, 'Sorted List Extraction')
    ], n, 'Extraction Time Comparison', ['red', 'blue', 'green'])
