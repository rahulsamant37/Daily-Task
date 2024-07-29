# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:

*   `KthLargest(int k, int[] nums)` Initializes the object with the integer k and the stream of integers nums.
*   `int add(int val)` Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

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
        # Initialize the KthLargest object with k and the initial stream of numbers.
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements.

        # Heapify the first k elements if available or all elements if less than k
        heapq.heapify(self.heap)

        # If the heap size is more than k, remove the smallest elements until only k elements remain.
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # Add a new value to the stream and return the kth largest element.

        # If the heap has less than k elements, simply add the new value.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Otherwise, if the new value is larger than the smallest element in the heap,
        # replace the smallest element with the new value.
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        # The kth largest element is always at the root of the min-heap.
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
    assert kthLargest3.add(4) == 3
    assert kthLargest3.add(2) == 3
    assert kthLargest3.add(2) == 3

if __name__ == "__main__":
    test_solution()