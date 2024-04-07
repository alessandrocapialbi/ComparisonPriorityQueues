from HeapPriorityQueue import HeapPriorityQueue
from LinkedListPriorityQueue import LinkedListPriorityQueue
from SortedLinkedListPriorityQueue import SortedLinkedListPriorityQueue
from PlotGenerator import PlotGenerator



if __name__ == "__main__":

    # Usage
    plot = PlotGenerator()

    num_elements = 10000 # Set desired dimensions

    pq_heap = HeapPriorityQueue()
    pq_unsorted_list = LinkedListPriorityQueue()
    pq_sorted_list = SortedLinkedListPriorityQueue()
    times = plot.measure_insertion_time(pq_heap, num_elements)
    plot.plot_insertion_time(times, num_elements, 'Heap')

