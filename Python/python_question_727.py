# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

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
        Initializes the KthLargest object with the given k and initial stream of numbers.
        We use a min-heap of size k to store the k largest elements seen so far.
        """
        self.k = k
        self.heap = []  # Min-heap to store the k largest elements
        for num in nums:
            self.add(num)  # Initialize the heap with the initial numbers

    def add(self, val: int) -> int:
        """
        Adds a new element to the stream and returns the kth largest element.
        """
        if len(self.heap) < self.k:
            # If the heap has fewer than k elements, simply add the new element.
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # If the new element is larger than the smallest element in the heap (root),
            # replace the smallest element with the new element and heapify.
            heapq.heapreplace(self.heap, val)

        # The root of the min-heap is always the kth largest element.
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
    assert kthLargest3.add(1) == 0
    assert kthLargest3.add(-4) == 0
    assert kthLargest3.add(-2) == -1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()