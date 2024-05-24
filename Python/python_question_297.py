# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream. Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Implement the KthLargest class:

*   `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
*   `int add(int val)` Appends the integer `val` to the stream and returns the element representing the k-th largest element in the stream.

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
        Initializes the KthLargest object with k and initial stream of numbers.

        Args:
            k: The k-th largest element to find.
            nums: The initial stream of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements
        heapq.heapify(self.heap)  # Transform list into a heap, in-place, in linear time

        # Keep only the k largest elements in the heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the k-th largest element.

        Args:
            val: The new element to add.

        Returns:
            The k-th largest element in the stream after adding the new element.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add to the heap if we have less than k elements
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element if val is larger

        return self.heap[0]  # The root of the min-heap is the k-th largest element


# Test cases
def test_solution():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    kthLargest2 = KthLargest(1, [])
    assert kthLargest2.add(-3) == -3
    assert kthLargest2.add(-2) == -2
    assert kthLargest2.add(-4) == -2
    assert kthLargest2.add(0) == 0
    assert kthLargest2.add(4) == 4

    kthLargest3 = KthLargest(2, [0])
    assert kthLargest3.add(-1) == -1
    assert kthLargest3.add(3) == 0
    assert kthLargest3.add(4) == 3
    assert kthLargest3.add(2) == 3
    assert kthLargest3.add(2) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()