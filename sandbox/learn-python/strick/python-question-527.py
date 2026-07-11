# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream. Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Implement the `KthLargest` class:

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
        Initializes the KthLargest object with k and the initial stream of numbers.

        Args:
            k: The k-th largest element to find.
            nums: The initial stream of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements.
        heapq.heapify(self.heap) # Transforms list into heap, in-place, in linear time

        # If the heap has more than k elements, remove the smallest elements
        # until only the k largest are left.
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # Remove the smallest element from the heap.

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the k-th largest element.

        Args:
            val: The new value to add to the stream.

        Returns:
            The k-th largest element in the updated stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add the new value to the heap.
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element with the new value if it's larger.

        return self.heap[0]  # The k-th largest element is always at the root of the min-heap.

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
    assert kthLargest.add(5) == 3
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 5
    assert kthLargest.add(4) == 4

    # Test case 4
    kthLargest = KthLargest(3, [5, -1])
    assert kthLargest.add(2) == -1
    assert kthLargest.add(1) == 1
    assert kthLargest.add(-1) == 1
    assert kthLargest.add(3) == 2
    assert kthLargest.add(4) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()