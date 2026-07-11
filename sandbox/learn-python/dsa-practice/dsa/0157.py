# DSA Problem 157

'''
Problem Statement:
A sequence of integers is called a zigzag sequence if each of its elements is either strictly greater than both neighbors or strictly less than both neighbors. For example, the sequence [1, 7, 4, 9, 2, 5] is a zigzag sequence. Given a list of integers, find the length of the longest subsequence that is a zigzag sequence.

Note: A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: nums = [1, 7, 4, 9, 2, 5]
Output: 6
Explanation: The entire array is a zigzag sequence.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
'''

Solution:
def longest_zigzag_subsequence(nums):
    n = len(nums)
    if n < 2:
        return n

    # Initialize two arrays, one for storing the length of the longest zigzag sequence ending with nums[i] and going up, and the other going down.
    up, down = [1] * n, [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                up[i] = max(up[i], down[j] + 1)
            elif nums[i] < nums[j]:
                down[i] = max(down[i], up[j] + 1)

    return max(max(up), max(down))

# Example check (the function can be tested with the example given in the problem statement)
nums = [1, 7, 4, 9, 2, 5]
print(longest_zigzag_subsequence(nums))  # Expected output: 6
'''

In this problem, I've created a dynamic programming solution to find the length of the longest zigzag subsequence in a given list of integers. The solution uses two arrays, `up` and `down`, to track the longest zigzag sequences ending at each index, either increasing or decreasing. This solution efficiently computes the maximum length of such a sequence in O(n^2) time complexity, which is optimal given the constraints.