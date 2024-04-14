# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) of `nums` whose sum equals `target`.  If no such subsequence exists, return 0.

An increasing subsequence is a sequence of elements from the original array where the elements are in strictly increasing order.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: 4
Explanation: The LIS [1, 2, 3, 3] doesn't work because it must be strictly increasing.  The LIS [1, 2, 3, 3] doesn't work because the sum is not equal to 9. The LIS [1, 2, 3] doesn't work because the sum is not equal to 9. The LIS [2, 3, 4] sums to 9 and has length 3. The LIS [1, 3, 5] sums to 9 and has length 3. However, the LIS [1, 2, 3, 3] sums to 9 and has length 3. The LIS [1, 2, 3, 3] doesn't work because it must be strictly increasing.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: No increasing subsequence sums to 10.

Input: nums = [2, 4, 6, 8, 10], target = 20
Output: 3
Explanation: The LIS [2, 8, 10] sums to 20 and has length 3. [4, 6, 10] also sums to 20 and has length 3. [2, 6, 12] does not work. [4, 8, 8] is not an increasing subsequence.
'''

# Solution
def solution():
    def longest_increasing_subsequence_sum(nums, target):
        """
        Finds the length of the longest increasing subsequence (LIS) of nums whose sum equals target.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            The length of the longest increasing subsequence with sum equal to target, or 0 if no such subsequence exists.
        """

        n = len(nums)
        dp = {}  # Memoization: (index, current_sum, last_element_used) -> length of LIS

        def solve(index, current_sum, last_element_used):
            """
            Recursive helper function to find the LIS length.

            Args:
                index: The current index in the nums array.
                current_sum: The current sum of the subsequence.
                last_element_used: The last element used in the subsequence (to maintain increasing order).

            Returns:
                The length of the LIS starting from the given index, with the given sum and last element used.
            """

            if current_sum == target:
                return 0  # Found a valid subsequence, return 0 to add to the length
            if index == n or current_sum > target:
                return float('-inf')  # Exceeded the target or reached the end, invalid subsequence

            if (index, current_sum, last_element_used) in dp:
                return dp[(index, current_sum, last_element_used)]

            # Option 1: Exclude the current element
            exclude = solve(index + 1, current_sum, last_element_used)

            # Option 2: Include the current element (if it's greater than the last element used)
            include = float('-inf')
            if nums[index] > last_element_used:
                include = 1 + solve(index + 1, current_sum + nums[index], nums[index]) # Add 1 to length

            dp[(index, current_sum, last_element_used)] = max(exclude, include)
            return dp[(index, current_sum, last_element_used)]

        result = solve(0, 0, float('-inf'))  # Start from index 0, sum 0, and no element used yet
        return max(0, result)  # Return 0 if no subsequence found (result is negative infinity)

    return longest_increasing_subsequence_sum
    

# Test cases
def test_solution():
    nums1 = [1, 2, 3, 4, 5]
    target1 = 9
    expected1 = 3
    assert solution()(nums1, target1) == expected1

    nums2 = [4, 3, 2, 1]
    target2 = 10
    expected2 = 0
    assert solution()(nums2, target2) == expected2

    nums3 = [2, 4, 6, 8, 10]
    target3 = 20
    expected3 = 3
    assert solution()(nums3, target3) == expected3

    nums4 = [1, 3, 5, 2, 4, 6]
    target4 = 12
    expected4 = 3
    assert solution()(nums4, target4) == 3

    nums5 = [1, 1, 1, 1, 1]
    target5 = 5
    expected5 = 0
    assert solution()(nums5, target5) == 0

    nums6 = [5, 6, 7, 8, 9]
    target6 = 21
    expected6 = 3
    assert solution()(nums6, target6) == 3

    nums7 = [1, 2, 3, 4, 5]
    target7 = 15
    expected7 = 5
    assert solution()(nums7, target7) == 5

    nums8 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    target8 = 10
    expected8 = 0
    assert solution()(nums8, target8) == 0

    nums9 = [1, 5, 2, 6, 3, 7, 4, 8]
    target9 = 15
    expected9 = 3
    assert solution()(nums9, target9) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()