# Python Question: Finding the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream of numbers.

The class should have the following methods:

*   `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the initial list of numbers `nums`.
*   `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the current k-th largest element.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

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
            k: The k-th largest element to find.
            nums: The initial list of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements
        heapq.heapify(self.heap) # Transform list into heap, in-place, in linear time
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Remove the smallest element until the heap size is k

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the k-th largest element.

        Args:
            val: The new value to add.

        Returns:
            The k-th largest element in the stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add the element if the heap is not full
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element if the new element is larger
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