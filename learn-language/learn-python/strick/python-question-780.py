# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream.

The class should have the following methods:

*   `KthLargest(int k, int[] nums)`: Initializes the object with the integer `k` and the initial stream `nums`.
*   `add(int val)`: Adds the integer `val` to the stream and returns the k-th largest element after the addition.

Note: You can assume that k is always valid, 1 ≤ k ≤ stream's length.

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
        # Initialize the min-heap with the first k elements or all elements if less than k
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)

        # If the initial list has more than k elements, adjust the heap
        for num in nums[k:]:
            if num > self.heap[0]:
                heapq.heapreplace(self.heap, num)

    def add(self, val: int) -> int:
        # If the heap is not yet full, add the element
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Otherwise, if the new element is larger than the smallest in the heap, replace it
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        # The root of the min-heap is always the k-th largest element
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
    assert kthLargest3.add(10) == 3
    assert kthLargest3.add(9) == 5
    assert kthLargest3.add(4) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()