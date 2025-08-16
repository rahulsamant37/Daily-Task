# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.

The class should have the following methods:

1.  `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the initial list of integers `nums`.
2.  `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the kth largest element in the current stream.

You are guaranteed that `k` is always valid, that is, `1 <= k <= len(current stream)`.

Example:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''

# Solution
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        """
        Initializes the KthLargest object.

        Args:
            k: The value of k (kth largest element to find).
            nums: The initial list of numbers.
        """
        self.k = k
        self.heap = nums[:k]  # Initialize heap with first k elements
        heapq.heapify(self.heap) # Transform list into a heap, in-place, in linear time

        # Add remaining elements to the heap, maintaining size k
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heapreplace(self.heap, num) # Replace smallest element with num and re-heapify

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Args:
            val: The new value to add.

        Returns:
            The kth largest element in the stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Test cases
def test_solution():
    # Test case 1
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    # Test case 2
    kthLargest = KthLargest(1, [])
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4

    # Test case 3
    kthLargest = KthLargest(2, [0])
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(3) == 0
    assert kthLargest.add(4) == 3
    assert kthLargest.add(2) == 3
    assert kthLargest.add(2) == 3

    # Test case 4 (k=1, large list)
    kthLargest = KthLargest(1, [5,2,9,1,5,6])
    assert kthLargest.add(7) == 9
    assert kthLargest.add(3) == 9
    assert kthLargest.add(10) == 10

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()