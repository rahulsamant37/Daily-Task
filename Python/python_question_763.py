# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) of `nums` such that the sum of the elements in the subsequence equals `target`. If no such subsequence exists, return 0.

An increasing subsequence is a sequence of numbers from the input array where each number is strictly greater than the previous number.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: 4
Explanation: The longest increasing subsequence with sum 10 is [1, 2, 3, 4], which has length 4.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: There is no increasing subsequence that sums to 10.

Input: nums = [2, 4, 6, 3, 5, 7], target = 12
Output: 3
Explanation: One possible LIS with sum 12 is [2, 3, 7], which has length 3.  Another is [5,7].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_sum(nums, target):
        """
        Finds the length of the longest increasing subsequence with a specific sum.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            The length of the longest increasing subsequence with sum equal to target.
            Returns 0 if no such subsequence exists.
        """

        n = len(nums)
        dp = {}  # Memoization: (index, current_sum, last_element) -> length of LIS

        def solve(index, current_sum, last_element):
            """
            Recursive function to find the length of the longest increasing subsequence.

            Args:
                index: The current index in the nums array.
                current_sum: The current sum of the subsequence.
                last_element: The last element added to the subsequence.

            Returns:
                The length of the longest increasing subsequence with sum equal to target,
                starting from the given index and following the given constraints.
            """

            if (index, current_sum, last_element) in dp:
                return dp[(index, current_sum, last_element)]

            if current_sum == target:
                return 0  # Found a subsequence with the target sum

            if index == n:
                return float('-inf')  # No more elements to consider

            # Option 1: Don't include the current element
            exclude = solve(index + 1, current_sum, last_element)

            # Option 2: Include the current element if it's greater than the last element
            include = float('-inf')
            if nums[index] > last_element and current_sum + nums[index] <= target:
                include = 1 + solve(index + 1, current_sum + nums[index], nums[index])

            dp[(index, current_sum, last_element)] = max(exclude, include)
            return dp[(index, current_sum, last_element)]

        result = solve(0, 0, float('-inf')) # Start from index 0, sum 0, and last element -infinity
        return max(0, result)  # If result is negative infinity, return 0

    return longest_increasing_subsequence_with_sum


# Test cases
def test_solution():
    nums1 = [1, 2, 3, 4, 5]
    target1 = 10
    assert solution()(nums1, target1) == 4

    nums2 = [4, 3, 2, 1]
    target2 = 10
    assert solution()(nums2, target2) == 0

    nums3 = [2, 4, 6, 3, 5, 7]
    target3 = 12
    assert solution()(nums3, target3) == 3

    nums4 = [1, 5, 2, 4, 3]
    target4 = 12
    assert solution()([1, 5, 2, 4, 3], 12) == 3

    nums5 = [1, 2, 3, 4, 5]
    target5 = 15
    assert solution()(nums5, target5) == 5

    nums6 = [10, 5, 2, 1, 3]
    target6 = 6
    assert solution()(nums6, target6) == 2

    nums7 = [1, 2, 3, 4, 5]
    target7 = 1
    assert solution()(nums7, target7) == 1

    nums8 = [5, 4, 3, 2, 1]
    target8 = 5
    assert solution()(nums8, target8) == 1

    nums9 = [1, 3, 5, 2, 4]
    target9 = 7
    assert solution()(nums9, target9) == 2

    nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target10 = 20
    assert solution()(nums10, target10) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()