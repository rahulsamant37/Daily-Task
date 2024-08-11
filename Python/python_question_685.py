# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream of numbers.

The class should have the following methods:

1.  `__init__(self, k: int, nums: List[int])`: Initializes the object with an integer k and an initial list of numbers nums.
2.  `add(self, val: int) -> int`: Appends the integer val to the stream and returns the kth largest element in the current stream.

You need to implement this efficiently. Using sorting for every `add` operation would be inefficient. Consider using a min-heap to maintain the k largest elements seen so far.

Example:

Input:
k = 3, nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
kthLargest.add(3)   # return 4
kthLargest.add(5)   # return 5
kthLargest.add(10)  # return 5
kthLargest.add(9)   # return 8
kthLargest.add(4)   # return 8
'''

# Solution
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        """
        Initializes the KthLargest object with k and an initial list of numbers.
        We use a min-heap (priority queue) to maintain the k largest elements seen so far.
        """
        self.k = k
        self.heap = nums[:k]  # Initialize heap with the first k elements
        heapq.heapify(self.heap)  # Transform list into a heap, in-place, in linear time

        # If the initial list has more than k elements, add the remaining elements
        # and maintain the heap size to be k.
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heapreplace(self.heap, num)

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the kth largest element.

        If the new element is larger than the smallest element in the heap (root of the min-heap),
        replace the root with the new element and heapify to maintain the min-heap property.

        Returns the current kth largest element, which is the root of the min-heap.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Test cases
def test_solution():
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    k = 1
    nums = []
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4

    k = 2
    nums = [0]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(1) == 0
    assert kthLargest.add(-2) == 0
    assert kthLargest.add(-4) == 0
    assert kthLargest.add(3) == 1

if __name__ == "__main__":
    test_solution()