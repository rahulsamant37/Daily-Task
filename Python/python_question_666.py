# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream. You will be given a list of initial numbers from the stream and an integer k. Implement the following methods:

*   `__init__(self, k: int, nums: List[int])`: Initializes the object with the integer `k` and the stream of integers `nums`.
*   `add(self, val: int) -> int`: Appends the integer `val` to the stream and returns the kth largest element in the current stream. If the stream has fewer than k elements, return the smallest element in the stream.

Example:

Input:
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)
kthLargest.add(3)   # returns 4
kthLargest.add(5)   # returns 5
kthLargest.add(10)  # returns 5
kthLargest.add(9)   # returns 8
kthLargest.add(4)   # returns 8
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
        self.heap = []  # Use a min-heap to store the k largest elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds a new number to the stream and returns the kth largest element.

        Args:
            val: The new number to add to the stream.

        Returns:
            The kth largest element in the current stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)  # Add to the heap if it's not full
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Replace the smallest element if the new value is larger

        if len(self.heap) < self.k:
            if not self.heap:
                return float('-inf') #Handle case where heap is empty.
            return min(self.heap)

        return self.heap[0]  # The smallest element in the heap is the kth largest


# Test cases
def test_solution():
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    k = 1
    nums = []
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4

    k = 2
    nums = [0]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-1) == -1
    assert kthLargest.add(3) == 0
    assert kthLargest.add(5) == 3
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 5
    assert kthLargest.add(4) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()