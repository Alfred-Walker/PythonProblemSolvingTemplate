"""heap sort using max heap

Python heapq module documentation:
   https://docs.python.org/2/library/heapq.html
"""

import heapq


class MaxHeapExample:
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

        """each value is pushed to the heap with the priority value"""
        for num in nums:
            heapq.heappush(heap, (-num, num))  # (heap, (priority, value))

        while heap:
            result.append(heapq.heappop(heap)[1])   # note that index [1] is specified

        return result


to_sort = [4, 1, 7, 3, 8, 5]
print(MaxHeapExample.heap_sort(to_sort))
# >>> [8, 7, 5, 4, 3, 1]
