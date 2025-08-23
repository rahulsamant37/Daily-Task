# DSA Problem 111

'''
Problem Statement:
Given a list of integers, find the longest subsequence where each element is exactly one more than the previous element and the subsequence is strictly increasing. If there are multiple subsequences of the same maximum length, return the one that appears first.

For example, in the list [1, 2, 3, 2, 3, 4, 5], the longest increasing consecutive subsequence is [2, 3, 4, 5].

Write a function `find_longest_consecutive_subsequence` that takes a list of integers and returns the longest increasing consecutive subsequence.
'''

Solution:
def find_longest_consecutive_subsequence(nums):
    if not nums:
        return []
    
    longest_seq = []
    current_seq = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_seq.append(nums[i])
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq[:]
        else:
            current_seq = [nums[i]]
    
    return longest_seq

# Example check function
def check_solution():
    assert find_longest_consecutive_subsequence([1, 2, 3, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert find_longest_consecutive_subsequence([10, 11, 12, 1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert find_longest_consecutive_subsequence([5, 4, 3, 2, 1]) == [1]
    assert find_longest_consecutive_subsequence([]) == []
    print("All tests passed!")

check_solution()