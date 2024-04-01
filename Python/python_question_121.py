# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream. Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Your KthLargest class will have:

*   A constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream.
*   A method add which accepts an integer val and returns the element representing the k-th largest element in the stream.

Example:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
'''

# Solution
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        """
        Initializes the KthLargest object with k and the initial stream nums.
        We use a min-heap to store the k largest elements seen so far.
        """
        self.k = k
        self.heap = nums  # Initialize heap with initial nums
        heapq.heapify(self.heap) # Convert list to heap in linear time
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Remove smallest element to maintain size k

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the k-th largest element.
        If the new element is larger than the smallest element in the heap,
        we replace the smallest element with the new element and heapify.
        Otherwise, we simply add the new element if the heap size is less than k.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val) # More efficient than pop then push
        return self.heap[0] # Top of min heap is kth largest

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