# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.
The class should have the following methods:

1.  `__init__(self, k: int, nums: List[int])`: Initializes the object with an integer k and an initial list of integers nums.
2.  `add(self, val: int) -> int`: Adds the new element val to the stream and returns the kth largest element in the stream.

You should use a min-heap data structure to efficiently maintain the k largest elements seen so far.

Example:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[None, 4, 5, 5, 8, 8]

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
            nums: The initial list of integers.
        """
        self.k = k
        self.heap = nums  # Use nums directly as the initial heap
        heapq.heapify(self.heap)  # Convert nums into a min-heap

        # If the heap has more than k elements, remove the smallest elements
        # until the heap size is k.  This ensures that the heap always
        # contains the k largest elements seen so far.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the kth largest element.

        Args:
            val: The new element to add.

        Returns:
            The kth largest element in the stream.
        """
        # If the heap has fewer than k elements, add the new element directly.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If the new element is larger than the smallest element in the heap,
        # replace the smallest element with the new element.
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        # The smallest element in the heap is always the kth largest element.
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
    assert kthLargest3.add(4) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()