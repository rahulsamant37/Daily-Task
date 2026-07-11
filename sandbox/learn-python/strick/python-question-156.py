# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.

You will be given an integer `k` and an initial array of integers `nums`.
Implement the following methods:

1.  `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the stream of integers `nums`.
2.  `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the kth largest element in the stream.

Example:
Input:
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
kthLargest.add(3)   # returns 4
kthLargest.add(5)   # returns 5
kthLargest.add(10)  # returns 5
kthLargest.add(9)   # returns 8
kthLargest.add(4)   # returns 8
'''

# Solution
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        """
        Initializes the KthLargest object.

        Args:
            k: The desired kth largest element.
            nums: The initial stream of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements
        heapq.heapify(self.heap)  # Transform list into heap, in-place, in linear time
        # Ensure the heap only contains the k largest elements initially
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Args:
            val: The value to add to the stream.

        Returns:
            The kth largest element in the stream after adding the value.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add to heap if there's space
        elif val > self.heap[0]:
            # If the new value is larger than the smallest element in the heap,
            # replace the smallest element with the new value.
            heapq.heapreplace(self.heap, val)

        return self.heap[0]  # The root of the min-heap is the kth largest element

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
    assert kthLargest.add(1) == 1
    assert kthLargest.add(2) == 2
    assert kthLargest.add(3) == 3
    assert kthLargest.add(4) == 4
    assert kthLargest.add(5) == 5

    k = 2
    nums = [0]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(3) == 0
    assert kthLargest.add(4) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()