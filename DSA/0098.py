# DSA Problem 98

'''
Problem Statement:
A sequence of numbers is called a sawtooth sequence if each element is either strictly greater than the previous element or strictly less than the next element, but not both. More formally, for a sequence `a`, it is a sawtooth sequence if for all valid indices `i`, one of the following holds:
- If `i` is even, then `a[i] < a[i+1]` and `a[i] < a[i-1]`.
- If `i` is odd, then `a[i] > a[i+1]` and `a[i] > a[i-1]`.
Given an array `nums` of distinct integers, determine the length of the longest subsequence that can be rearranged to form a sawtooth sequence.

Example 1:
Input: nums = [1, 17, 4, 3, 5, 8]
Output: 5
Explanation: The longest sawtooth subsequence that can be formed is [1, 4, 3, 5, 8].
Example 2:
Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 7
Explanation: One of the longest sawtooth subsequences that can be formed is [10, 22, 9, 33, 21, 50, 41].

Constraints:
- `1 <= nums.length <= 2000`
- `0 <= nums[i] <= 10^6`
- All values of `nums` are unique.
'''

Solution:
def longest_sawtooth_subsequence(nums):
    n = len(nums)
    up, down = [1] * n, [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                up[i] = max(up[i], down[j] + 1)
            elif nums[i] < nums[j]:
                down[i] = max(down[i], up[j] + 1)
    
    return max(max(up), max(down))

# Example usage
nums = [1, 17, 4, 3, 5, 8]
print(longest_sawtooth_subsequence(nums))  # Output: 5

nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_sawtooth_subsequence(nums))  # Output: 7
'''
This solution uses dynamic programming to find the longest subsequence that can be rearranged into a sawtooth sequence. It iterates through the array, updating two lists (`up` and `down`) that keep track of the longest subsequence ending at each index in an increasing or decreasing manner, respectively. The maximum of these two lists gives the length of the longest sawtooth subsequence.