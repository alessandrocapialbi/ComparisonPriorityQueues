Sorted Linked List, Unsorted Linked List and Max-Heap Implementations in Python
This Python project provides flexible and robust implementations of:

Sorted Linked List: Maintains elements in ascending order for efficient access.
Unsorted Linked List: Offers fast insertions without concern for order.
Max-Heap (list-based): A tree-like data structure ensuring quick access to the maximum value.
Key Features
Modularity: Each data structure is implemented in a separate class for easy maintenance and reuse.
Comprehensive Operations: Supports insertion, search and extraction of the maximum value, iteration, and other operations specific to each data structure.

Clone the Repository:

Bash
git clone https://github.com/alessandro_capialbi/ComparisonPriorityQueues.git
Use code with caution.
content_copy

Import the Classes:

Python
from linked_list import SortedLinkedList, UnsortedLinkedList
from max_heap import HeapPriorityQueue
Use code with caution.
play_circleeditcontent_copy
Create and Manipulate the Data Structures:

Python
# Sorted linked list
sorted_list = SortedLinkedListQueue()
sorted_list.insert(5)
sorted_list.insert(2)
sorted_list.insert(8)

# Unsorted linked list
unsorted_list = UnsortedLinkedListQueue()
unsorted_list.insert(1)
unsorted_list.insert(7)
unsorted_list.insert(3)

# Max-heap
heap = HeapPriorityQueue()
heap.insert(10)
heap.insert(3)
heap.insert(15)
max_value = heap.extract_max()
Use code with caution.
play_circleeditcontent_copy

License
This project is released under the MIT License.
