# DSA Problem generated on 2024-11-19

Here's a unique DSA problem in Python with a solution:

**Problem Statement:**

**Minimum Operations to Make Array Elements Equal**

Given an array of integers, find the minimum number of operations required to make all elements of the array equal. An operation is defined as either incrementing or decrementing an element by 1.

**Example:**

Input: `[3, 5, 2, 7]`

Output: `6`

Explanation: One possible sequence of operations is:

* Decrement 5 to 3 (1 operation)
* Decrement 7 to 5 (2 operations)
* Decrement 5 to 3 (1 operation)
* Increment 2 to 3 (1 operation)

Total operations: 6

**Solution Code:**
```python
def min_operations_to_equality(arr):
    median = sorted(arr)[len(arr) // 2]
    operations = 0
    for num in arr:
        operations += abs(num - median)
    return operations
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n log n), where n is the length of the input array.

Here's the breakdown:

* The `sorted` function takes O(n log n) time to sort the array.
* The loop iterates over the array, which takes O(n) time.
* The `abs` function and subtraction operations take constant time.

Since the sorting operation dominates the time complexity, the overall time complexity is O(n log n).

**Why this solution works:**

The key insight is that the median of the array is the value that minimizes the sum of absolute differences with all other elements. By making all elements equal to the median, we minimize the total number of operations required.

For example, in the input `[3, 5, 2, 7]`, the median is 3. We can see that making all elements equal to 3 requires the minimum number of operations: 6.

This problem is a variation of the classic "median finding" problem, with an added twist of minimizing operations. The solution uses the median as a pivot to minimize the sum of absolute differences, which is a common technique in optimization problems.