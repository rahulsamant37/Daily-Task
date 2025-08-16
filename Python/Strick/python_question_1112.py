# Python Question: Find the Kth Largest Element in a Stream
'''
Design a class to find the kth largest element in a stream.

Implement the KthLargest class:

*   KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
*   int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the updated stream.  If the stream has fewer than k elements, return the smallest element in the stream.

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
            k: The desired kth largest element.
            nums: The initial stream of numbers.
        """
        self.k = k
        self.heap = nums  # Use a min-heap to store the k largest elements.
        heapq.heapify(self.heap)  # Convert the list into a heap in-place.
        while len(self.heap) > k:
            heapq.heappop(self.heap) # Ensure only k largest elements are in the heap initially


    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Args:
            val: The new value to add to the stream.

        Returns:
            The kth largest element in the updated stream.
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val) # If we have fewer than k elements, add the new element
        elif val > self.heap[0]:  # If the new value is larger than the smallest element in the heap
            heapq.heapreplace(self.heap, val)  # Replace the smallest with the new value

        if len(self.heap) < self.k:
            return min(self.heap) if self.heap else None
        return self.heap[0]  # The root of the min-heap is the kth largest element.


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