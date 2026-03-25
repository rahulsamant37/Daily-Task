# DSA Problem 315

'''
Problem Statement:
Given a list of integers, find the length of the longest subsequence such that the elements in the subsequence are consecutive integers, regardless of their indices in the original list. Consecutive elements can be in any order within the subsequence. 

For example, in the list [1, 9, 3, 10, 4, 20, 2], the longest subsequence of consecutive elements is [1, 3, 4, 2], and the length of this subsequence is 4. Note that the elements do not need to be in order in the original list.
'''

Solution:
def longest_consecutive_subsequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if it is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_subsequence(nums))  # Output: 4

# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
This solution works as follows:
1. Convert the list to a set for O(1) lookups.
2. For each number in the set, check if it's the start of a sequence (i.e., there's no preceding number).
3. If it is, count how many numbers follow in sequence.
4. Keep track of the longest sequence found.
5. Return the length of the longest sequence.
'''