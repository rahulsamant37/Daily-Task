# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.

You will be given an integer k and an integer array nums which represents initial elements from the stream.

The class should have the following methods:

*   `KthLargest(int k, int[] nums)`: Initializes the object with the integer k and the stream array nums.
*   `int add(int val)`: Appends the integer val to the stream and returns the element representing the kth largest element in the stream. If the stream has less than k elements, return the smallest element currently in the stream.

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
        self.heap = nums
        heapq.heapify(self.heap)  # Transform list into a heap, in-place, in linear time
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Remove the smallest element until the heap has size k

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the kth largest element.

        Args:
            val: The new element to add to the stream.

        Returns:
            The kth largest element in the stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add the new element to the heap
        elif val > self.heap[0]: # if val > smallest element in heap
            heapq.heapreplace(self.heap, val) # replace smallest element with val
        return self.heap[0]

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
    assert kthLargest3.add(5) == 3
    assert kthLargest3.add(10) == 5
    assert kthLargest3.add(9) == 5
    assert kthLargest3.add(4) == 5

if __name__ == "__main__":
    test_solution()