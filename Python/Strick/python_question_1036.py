# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.  You will be given a stream of numbers, and you need to efficiently determine the kth largest number seen so far at each step.

Implement the `KthLargest` class:

*   `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the initial stream `nums`.
*   `int add(int val)` Appends the integer `val` to the stream and returns the element representing the kth largest element in the stream.

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
            k: The kth largest element to find.
            nums: The initial stream of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements
        heapq.heapify(self.heap) # Transform list into heap, in-place, in linear time

        # Maintain the heap size to be at most k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the kth largest element.

        Args:
            val: The new element to add.

        Returns:
            The kth largest element in the stream after adding the new element.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val) # More efficient than pop and push

        return self.heap[0]  # The root of the min-heap is the kth largest element

# Test cases
def test_solution():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    kthLargest = KthLargest(1, [])
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4

    kthLargest = KthLargest(2, [0])
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(3) == 0
    assert kthLargest.add(5) == 3
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 5
    assert kthLargest.add(4) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()