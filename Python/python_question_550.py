# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.  Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:

*   KthLargest(int k, int[] nums) Initializes the object with the integer k and the initial stream nums.
*   int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

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
        Initializes the KthLargest object with k and the initial stream nums.

        The approach is to maintain a min-heap of size k.
        The elements in the heap are the k largest elements seen so far.
        The root of the heap will always be the kth largest element.
        """
        self.k = k
        self.heap = nums  # Initialize the heap with the given numbers
        heapq.heapify(self.heap)  # Transform the list into a heap, in-place, in linear time
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # Remove the smallest elements until the heap size is k

    def add(self, val: int) -> int:
        """
        Adds val to the stream and returns the kth largest element.

        If the heap has less than k elements, add the new value to the heap.
        Otherwise, if the new value is greater than the smallest element in the heap,
        replace the smallest element with the new value.
        Finally, return the root of the heap (the kth largest element).
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add the new element to the heap
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element in the heap with the new value

        return self.heap[0]  # Return the kth largest element (root of the heap)


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
    assert kthLargest.add(4) == 5

    # Test case 4
    kthLargest = KthLargest(3, [5,-1])
    assert kthLargest.add(2) == -1
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(3) == 2
    assert kthLargest.add(4) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()