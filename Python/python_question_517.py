# Python Question: Find the Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the longest increasing subsequence (LIS) of `nums` whose sum equals the `target`. If multiple such subsequences exist with the same length, return any one of them. If no such subsequence exists, return an empty list.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: [1, 2, 3, 3] or [4, 5]  (Both are valid LIS summing to 9)
Input: nums = [4, 3, 5, 1, 2], target = 8
Output: [3, 5]
Input: nums = [1, 5, 2, 6, 3, 7, 4], target = 10
Output: [1, 2, 3, 4]
Input: nums = [1, 2, 3], target = 10
Output: []
'''

# Solution
def solution():
    def find_longest_increasing_subsequence_with_sum(nums, target):
        """
        Finds the longest increasing subsequence (LIS) of nums whose sum equals the target.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            A list representing the LIS, or an empty list if no such subsequence exists.
        """

        n = len(nums)
        dp = {}  # dp[(i, s)] stores the longest increasing subsequence ending at index i with sum s

        def solve(index, current_sum):
            """
            Recursive helper function to find the LIS.

            Args:
                index: The current index in the nums array.
                current_sum: The current sum of the subsequence being built.

            Returns:
                A list representing the LIS, or None if no such subsequence exists.
            """
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]

            if current_sum == target:
                return []  # Found a subsequence with the target sum

            if index == n:
                return None  # Reached the end of the array without finding the target sum

            # Option 1: Exclude the current number
            exclude = solve(index + 1, current_sum)

            # Option 2: Include the current number (if possible)
            include = None
            if current_sum + nums[index] <= target:
                # Check if the current number can be added to the subsequence
                # The subsequence must be increasing
                can_include = True
                if exclude is not None or include is not None:
                  if exclude is not None and len(exclude) > 0 :
                    if index > 0 and len(exclude) > 0 and nums[index] <= nums[index-1]:
                      can_include = False
                if can_include:
                    sub_result = solve(index + 1, current_sum + nums[index])
                    if sub_result is not None:
                        include = [nums[index]] + sub_result

            # Choose the longer subsequence
            if include is None and exclude is None:
                dp[(index, current_sum)] = None
                return None
            elif include is None:
                dp[(index, current_sum)] = exclude
                return exclude
            elif exclude is None:
                dp[(index, current_sum)] = include
                return include
            else:
                dp[(index, current_sum)] = include if len(include) > len(exclude) else exclude
                return include if len(include) > len(exclude) else exclude

        result = solve(0, 0)
        if result is None:
            return []
        else:
            # Verify increasing property
            is_increasing = True
            for i in range(len(result) - 1):
                if result[i] >= result[i+1]:
                    is_increasing = False
                    break
            if is_increasing:
              return result
            else:
              return []


    # Test cases
    def test_solution():
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 9) in [[4, 5], [2, 3, 4]]
        assert find_longest_increasing_subsequence_with_sum([4, 3, 5, 1, 2], 8) == [3, 5]
        assert find_longest_increasing_subsequence_with_sum([1, 5, 2, 6, 3, 7, 4], 10) == [1, 2, 3, 4]
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3], 10) == []
        assert find_longest_increasing_subsequence_with_sum([1, 3, 5, 2, 4], 6) == [1, 5]
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 1) == [1]
        assert find_longest_increasing_subsequence_with_sum([5, 4, 3, 2, 1], 15) == []
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 15) == [1, 2, 3, 4, 5]
        assert find_longest_increasing_subsequence_with_sum([2, 4, 6, 8, 10], 20) == [2, 4, 6, 8]
        assert find_longest_increasing_subsequence_with_sum([2, 4, 6, 8, 10], 30) == []
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 1, 2, 3], 6) in [[1, 2, 3], [1, 2, 3]]
        assert find_longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert find_longest_increasing_subsequence_with_sum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 55) == []
        assert find_longest_increasing_subsequence_with_sum([1, 3, 2, 4, 5], 12) == [3, 4, 5]
        assert find_longest_increasing_subsequence_with_sum([1, 2, 5, 3, 4], 10) == [1, 2, 3, 4]

        print("All test cases passed!")

    if __name__ == "__main__":
        test_solution()