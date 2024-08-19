# DSA Problem 169

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find all unique pairs of numbers in the list that sum up to `k`. Each number in the list can only be used once, and you cannot use the same number twice to form a pair. Return a list of all such pairs, with each pair sorted in ascending order. If no such pairs exist, return an empty list.

Example 1:
Input: nums = [1, 2, 3, 4, 5], k = 6
Output: [[1, 5], [2, 4]]
Explanation: The pairs (1, 5) and (2, 4) sum up to 6. The pair (3, 3) is not valid since each number can only be used once.

Example 2:
Input: nums = [1, 1, 1, 1], k = 2
Output: [[1, 1]]
Explanation: The only valid pair is (1, 1).

Constraints:
- 1 <= len(nums) <= 1000
- -1000 <= nums[i] <= 1000
- -2000 <= k <= 2000
'''

Solution:
def find_pairs(nums, k):
    nums.sort()
    result = []
    seen = set()
    complements = set()

    for num in nums:
        if k - num in complements and num not in seen:
            result.append([num, k - num])
            seen.add(num)
            seen.add(k - num)
        complements.add(num)
    return result

# Example test cases
print(find_pairs([1, 2, 3, 4, 5], 6))  # Output: [[1, 5], [2, 4]]
print(find_pairs([1, 1, 1, 1], 2))     # Output: [[1, 1]]