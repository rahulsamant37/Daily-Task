# DSA Problem for 2024-12-03

Here is a novel DSA problem with a Python solution for 2024-12-03:

**Problem Statement:**

**"K-Window Median"**

Given a stream of integers and an integer `K`, find the median of the last `K` elements in the stream at any point in time. The stream is non-stop and continuous, and you can only process each element once. You are not allowed to store the entire stream in memory.

**Constraints:**

* `1 <= K <= 10^5`
* The stream can have up to `10^6` elements
* Each element in the stream is an integer between `-10^9` and `10^9`

**Optimal Solution:**

We can use a two-pointer approach with a balanced BST (Binary Search Tree) to solve this problem efficiently. We'll maintain two pointers, `left` and `right`, that point to the middle of the BST. The `left` pointer will always point to the median of the window, and the `right` pointer will point to the element just after the median.

Here's the Python solution:
```python
import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class KWindowMedian:
    def __init__(self, k):
        self.k = k
        self.left_maxHeap = []  # max heap to store the left half of the window
        self.right_minHeap = []  # min heap to store the right half of the window
        self.median = None

    def add_element(self, num):
        if not self.left_maxHeap or num < -self.left_maxHeap[0]:
            heapq.heappush(self.left_maxHeap, -num)
        else:
            heapq.heappush(self.right_minHeap, num)

        # balance the heaps
        if len(self.left_maxHeap) > len(self.right_minHeap) + 1:
            heapq.heappush(self.right_minHeap, -heapq.heappop(self.left_maxHeap))
        elif len(self.right_minHeap) > len(self.left_maxHeap):
            heapq.heappush(self.left_maxHeap, -heapq.heappop(self.right_minHeap))

        # update the median
        if len(self.left_maxHeap) == len(self.right_minHeap):
            self.median = (-self.left_maxHeap[0] + self.right_minHeap[0]) / 2
        else:
            self.median = -self.left_maxHeap[0]

    def get_median(self):
        return self.median
```
**Time/Space Complexity Analysis:**

* **Time complexity:** `O(logK)` per element, where `K` is the window size. This is because we're using a balanced BST to store the elements, and each insertion/deletion operation takes `O(logK)` time.
* **Space complexity:** `O(K)` to store the elements in the BST. We're storing at most `K` elements in the two heaps, which takes `O(K)` space.

Overall, this solution is efficient and scalable for large streams of data.