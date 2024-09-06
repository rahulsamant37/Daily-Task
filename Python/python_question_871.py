# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the longest increasing subsequence (LIS) in `nums` such that the sum of the elements in the subsequence equals `target`.  If no such subsequence exists, return an empty list.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 7
Output: [2, 5]

Input: nums = [1, 3, 2, 4, 5], target = 7
Output: [3, 4]

Input: nums = [1, 2, 3, 4, 5], target = 20
Output: []
'''

# Solution
def solution():
    def find_lis_with_sum(nums, target):
        """
        Finds the longest increasing subsequence (LIS) in `nums` such that the sum of the elements in the subsequence equals `target`.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            A list representing the longest increasing subsequence with the target sum, or an empty list if no such subsequence exists.
        """

        n = len(nums)
        dp = {}  # dp[(index, remaining_sum)] = (length, subsequence)

        def solve(index, remaining_sum):
            """
            Recursive helper function to find the LIS with the given remaining sum.

            Args:
                index: The current index in the nums array.
                remaining_sum: The remaining sum to achieve.

            Returns:
                A tuple containing the length of the LIS and the LIS itself.
            """

            if (index, remaining_sum) in dp:
                return dp[(index, remaining_sum)]

            if remaining_sum == 0:
                return 0, []  # Found a subsequence with the target sum

            if index == n:
                return -1, []  # Reached the end of the array without finding the target sum

            # Option 1: Exclude the current element
            len_exclude, seq_exclude = solve(index + 1, remaining_sum)

            # Option 2: Include the current element if it's possible
            len_include = -1
            seq_include = []
            if nums[index] <= remaining_sum:
                len_prev, seq_prev = 0, []
                can_include = True
                if seq_exclude:
                    if seq_exclude and len(seq_exclude) > 0 and nums[index] >= seq_exclude[0]:
                         can_include = False

                if can_include:
                    len_include, seq_include = solve(index + 1, remaining_sum - nums[index])
                    if len_include != -1:
                        len_include += 1
                        seq_include = [nums[index]] + seq_include


            # Choose the option with the longer subsequence
            if len_include > len_exclude:
                dp[(index, remaining_sum)] = len_include, seq_include
            else:
                dp[(index, remaining_sum)] = len_exclude, seq_exclude

            return dp[(index, remaining_sum)]

        length, subsequence = solve(0, target)

        if length == -1:
            return []
        else:
            sorted_subsequence = sorted(subsequence)

            is_increasing = True
            if len(sorted_subsequence) > 1:
                for i in range(len(sorted_subsequence) - 1):
                    if sorted_subsequence[i] >= sorted_subsequence[i+1]:
                        is_increasing = False
                        break

            if is_increasing:
                return sorted_subsequence
            else:
                return []
    
    return find_lis_with_sum

# Test cases
def test_solution():
    find_lis_with_sum = solution()
    assert find_lis_with_sum([1, 2, 3, 4, 5], 7) == [2, 5]
    assert find_lis_with_sum([1, 3, 2, 4, 5], 7) == [3, 4]
    assert find_lis_with_sum([1, 2, 3, 4, 5], 20) == []
    assert find_lis_with_sum([5, 4, 3, 2, 1], 7) == []
    assert find_lis_with_sum([1, 5, 2, 6, 3, 7, 4], 10) == [1, 2, 3, 4]
    assert find_lis_with_sum([1, 2, 3, 4, 5], 6) == [1, 2, 3]
    assert find_lis_with_sum([10, 22, 9, 33, 21, 50, 41, 60, 80], 133) == [22, 33, 41, 37]
    assert find_lis_with_sum([1, 2, 3], 4) == [1, 3]
    assert find_lis_with_sum([1, 2, 3, 4, 5, 6, 7], 15) == [1, 2, 3, 4, 5]
    assert find_lis_with_sum([1,2,3,4,5], 1) == [1]
    assert find_lis_with_sum([2, 3, 5, 1, 6, 8, 9], 16) == [2, 5, 9]
    assert find_lis_with_sum([3, 4, 1, 8, 2, 9, 7], 15) == [1, 7]
    assert find_lis_with_sum([2, 3, 4, 5, 6], 10) == [4, 6]
    assert find_lis_with_sum([2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == [2, 3, 5, 10]
    assert find_lis_with_sum([5, 1, 4, 2, 3], 7) == [1, 2, 3]
    assert find_lis_with_sum([1, 2, 3, 4, 5], 1) == [1]
    assert find_lis_with_sum([1, 2, 3, 4, 5], 0) == []

if __name__ == "__main__":
    test_solution()