# DSA Problem 327

'''
Problem Statement:
A sequence of positive integers is called harmonious if the difference between the maximum and the minimum element is exactly 1. Given a list of positive integers, find the length of the longest harmonious subsequence. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
'''

Solution:
def findLHS(nums):
    from collections import Counter
    count = Counter(nums)
    res = 0
    for num in count:
        if num + 1 in count:
            res = max(res, count[num] + count[num + 1])
    return res

# Test the solution
nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))  # Output should be 5

# Explanation:
# This solution works by first counting the occurrences of each number using a Counter from the collections module.
# Then, it checks if there exists a number in the list that is exactly 1 greater than the current number.
# If such a number exists, it calculates the length of the harmonious subsequence that can be formed by these two numbers and updates the maximum length found so far.
# Finally, it returns the maximum length of any harmonious subsequence found in the list.
# The time complexity is O(n) where n is the number of elements in the input list, since each number is processed a constant number of times.
# The space complexity is O(n) for storing the counts in the Counter.