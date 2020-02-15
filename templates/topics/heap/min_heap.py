"""heap sort using max heap

Python heapq module documentation:
   https://docs.python.org/2/library/heapq.html
"""

import heapq


class MinHeapExample:
    """
        1. Height of the heap tree: log2(n), complete binary tree
        2. time to insert or to delete: log2(n)
        3. Time Complexity (Best / Avg / Worst): n log2(n) / n log2(a)/n log2(a)
        4. Note that the largest element at index 0 does not guarantee that index 1 has the second largest element.
        (same for 3rd, 4th, and etc.)
    """
    @staticmethod
    def heap_sort(nums):
        heap = []
        result = []

        for num in nums:
            heapq.heappush(heap, num)   # in case of explicit priority, see 'max_heap.py'

        while heap:
            result.append(heapq.heappop(heap))  # in case of explicit priority, see 'max_heap.py'

        return result


to_sort = [4, 1, 7, 3, 8, 5]
print(MinHeapExample.heap_sort(to_sort))
# >>> [1, 3, 4, 5, 7, 8]
