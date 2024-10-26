# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream. Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Implement the KthLargest class:

*   KthLargest(int k, int[] nums) Initializes the object with the integer k and the initial stream nums.
*   int add(int val) Appends the integer val to the stream and returns the element representing the k-th largest element in the stream.

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
        Uses a min-heap of size k to store the k largest elements seen so far.
        """
        self.k = k
        self.heap = []  # Min-heap to store k largest elements

        # Initialize the heap with the initial nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds the integer val to the stream and returns the k-th largest element in the stream.

        If the heap has less than k elements, add the new element.
        If the new element is larger than the smallest element in the heap,
        replace the smallest element with the new element.

        Returns the smallest element in the heap (which is the k-th largest element seen so far).
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add to heap if size < k
        elif val > self.heap[0]:  # If val is larger than the smallest element in the heap
            heapq.heapreplace(self.heap, val)  # Replace the smallest with val

        return self.heap[0]  # Return the k-th largest element

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