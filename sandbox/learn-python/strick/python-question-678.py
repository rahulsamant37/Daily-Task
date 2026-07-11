# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the k-th largest element in a stream.  You will be given an integer `k` and an initial array of integers `nums`.
The class should have two methods:

1.  `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the stream of integers `nums`.
2.  `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the k-th largest element in the current stream.

Note that it is the k-th largest element in the *sorted order*, not the k-th distinct element.

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
            nums: The initial stream of integers.
        """
        self.k = k
        self.heap = []  # Use a min-heap to store the k largest elements seen so far

        # Initialize the heap with the elements in nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds the integer `val` to the stream and returns the k-th largest element in the current stream.

        Args:
            val: The integer to add to the stream.

        Returns:
            The k-th largest element in the current stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add to heap if heap size is less than k
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element if val is larger

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
    assert kthLargest3.add(5) == 3
    assert kthLargest3.add(10) == 3
    assert kthLargest3.add(9) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()