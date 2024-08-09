# Python Question: Find the Longest Increasing Subsequence with a Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the longest increasing subsequence (LIS) within `nums` that sums up to the `target`. If no such subsequence exists, return an empty list.
If multiple LIS's with the target sum exist, return the one with the smallest starting index.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 7
Output: [2, 5]

Input: nums = [1, 3, 2, 4, 5], target = 7
Output: [1, 2, 4]

Input: nums = [5, 3, 1, 4, 2], target = 7
Output: [3, 4]

Input: nums = [1, 2, 3, 4, 5], target = 15
Output: [1, 2, 3, 4, 5]

Input: nums = [1, 2, 3, 4, 5], target = 1
Output: [1]

Input: nums = [1, 2, 3, 4, 5], target = 0
Output: []

Input: nums = [5, 1, 2, 3, 4], target = 10
Output: [1, 2, 3, 4]

Input: nums = [10, 5, 2, 3, 1], target = 6
Output: [5, 1]
'''

# Solution
def find_longest_increasing_subsequence_with_sum(nums, target):
    """
    Finds the longest increasing subsequence (LIS) within `nums` that sums up to the `target`.

    Args:
        nums: A list of positive integers.
        target: The target sum.

    Returns:
        A list representing the LIS that sums to the target, or an empty list if no such subsequence exists.
    """

    n = len(nums)
    longest_subsequence = []

    def backtrack(index, current_subsequence, current_sum):
        """
        Recursive backtracking function to explore all possible increasing subsequences.

        Args:
            index: The current index in the `nums` array.
            current_subsequence: The current subsequence being built.
            current_sum: The sum of the elements in the current subsequence.
        """
        nonlocal longest_subsequence

        # Base case: If the target sum is reached
        if current_sum == target:
            # Check if the current subsequence is longer than the best one found so far
            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence[:]  # Make a copy to avoid modification issues
            elif len(current_subsequence) == len(longest_subsequence) and current_subsequence:
                # if the starting indices are the same length, return the one with the smallest starting index
                if len(longest_subsequence) > 0:
                  first_index_current = nums.index(current_subsequence[0])
                  first_index_longest = nums.index(longest_subsequence[0])
                  if first_index_current < first_index_longest:
                    longest_subsequence = current_subsequence[:]

            return

        # Base case: If the target sum is exceeded or the end of the array is reached
        if current_sum > target or index == n:
            return

        # Explore two options: include the current element or exclude it
        # 1. Exclude the current element
        backtrack(index + 1, current_subsequence, current_sum)

        # 2. Include the current element, but only if it maintains the increasing order
        if not current_subsequence or nums[index] > current_subsequence[-1]:
            backtrack(index + 1, current_subsequence + [nums[index]], current_sum + nums[index])

    backtrack(0, [], 0)  # Start the backtracking from the beginning of the array

    return longest_subsequence

# Test cases
def test_solution():
    assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 7) == [2, 5]
    assert find_longest_increasing_subsequence_with_sum([1, 3, 2, 4, 5], 7) == [1, 2, 4]
    assert find_longest_increasing_subsequence_with_sum([5, 3, 1, 4, 2], 7) == [3, 4]
    assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 1) == [1]
    assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 0) == []
    assert find_longest_increasing_subsequence_with_sum([10, 5, 2, 3, 1], 6) == [5, 1]
    assert find_longest_increasing_subsequence_with_sum([5, 1, 2, 3, 4], 10) == [1, 2, 3, 4]
    assert find_longest_increasing_subsequence_with_sum([4, 3, 5, 1, 2, 7], 12) == [3, 5, 4]
    assert find_longest_increasing_subsequence_with_sum([1, 5, 2, 6, 3, 7], 10) == [1, 2, 7]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()