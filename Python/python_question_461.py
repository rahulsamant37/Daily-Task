# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) of `nums` such that the sum of the elements in the subsequence equals the `target`. If no such subsequence exists, return 0.

An increasing subsequence is a sequence of elements from the array `nums` where the elements are in strictly increasing order.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: 4
Explanation: The longest increasing subsequence with sum 9 is [1, 2, 3, 4], which has length 4.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: There is no increasing subsequence with sum 10.

Input: nums = [2, 4, 6, 8, 10], target = 12
Output: 2
Explanation: The longest increasing subsequence with sum 12 is [2, 10] or [4, 8], which has length 2.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_sum(nums, target):
        """
        Finds the length of the longest increasing subsequence of nums with sum equal to target.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            The length of the longest increasing subsequence with sum equal to target, or 0 if no such subsequence exists.
        """

        n = len(nums)
        dp = {}  # Key: (index, current_sum, last_element), Value: length of LIS

        def solve(index, current_sum, last_element):
            """
            Recursive helper function to find the length of the LIS.

            Args:
                index: The current index in the nums array.
                current_sum: The sum of the elements in the current subsequence.
                last_element: The last element added to the current subsequence.

            Returns:
                The length of the LIS starting from the given index with the given current sum and last element.
            """

            if (index, current_sum, last_element) in dp:
                return dp[(index, current_sum, last_element)]

            if current_sum == target:
                return 0  # We found a subsequence with the target sum. Start counting its length from next elements.

            if index == n:
                return float('-inf')  # No valid subsequence found, return negative infinity to be ignored.

            # Option 1: Exclude the current element
            exclude = solve(index + 1, current_sum, last_element)

            # Option 2: Include the current element if it's greater than the last element and adding it doesn't exceed target
            include = float('-inf')
            if nums[index] > last_element and current_sum + nums[index] <= target:
                include = 1 + solve(index + 1, current_sum + nums[index], nums[index])

            dp[(index, current_sum, last_element)] = max(exclude, include)
            return dp[(index, current_sum, last_element)]

        result = solve(0, 0, float('-inf'))  # Start from index 0, sum 0, and no last element
        return result if result > 0 else 0  # Return result if positive (found a LIS), otherwise return 0

    return longest_increasing_subsequence_with_sum


# Test cases
def test_solution():
    nums1 = [1, 2, 3, 4, 5]
    target1 = 9
    expected1 = 4
    assert solution()(nums1, target1) == expected1

    nums2 = [4, 3, 2, 1]
    target2 = 10
    expected2 = 0
    assert solution()(nums2, target2) == expected2

    nums3 = [2, 4, 6, 8, 10]
    target3 = 12
    expected3 = 2
    assert solution()(nums3, target3) == expected3

    nums4 = [1, 3, 5, 2, 4]
    target4 = 8
    expected4 = 3
    assert solution()(nums4, target4) == 3

    nums5 = [1, 10, 2, 3, 4, 5]
    target5 = 15
    expected5 = 4
    assert solution()(nums5, target5) == 4

    nums6 = [1, 2, 3, 4, 5]
    target6 = 1
    expected6 = 1
    assert solution()(nums6, target6) == 1

    nums7 = [5, 4, 3, 2, 1]
    target7 = 5
    expected7 = 1
    assert solution()(nums7, target7) == 1

    nums8 = [1, 2, 3]
    target8 = 6
    expected8 = 3
    assert solution()(nums8, target8) == 3

    nums9 = [1, 5, 2, 3, 4]
    target9 = 12
    expected9 = 4
    assert solution()(nums9, target9) == 4

    nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target10 = 20
    expected10 = 5
    assert solution()(nums10, target10) == 5

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()