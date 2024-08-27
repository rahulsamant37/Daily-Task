# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the sum of this LIS.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The longest increasing subsequence with the maximum sum is [1, 2, 3, 100], which has a sum of 106.  Another LIS is [1, 2, 3, 4, 5] which has a sum of 15.  The LIS we want is the one that maximizes the sum, which is [1, 2, 3, 100].

Input: nums = [10, 5, 4, 3]
Output: 10
Explanation: The longest increasing subsequence is just the element itself, so we choose 10 since it's the largest.

Input: nums = [1, 3, 2, 4, 5]
Output: 15
Explanation: The longest increasing subsequence is [1, 2, 4, 5] or [1, 3, 4, 5].  The second one has the largest sum of 13.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_max_sum(nums):
        """
        Finds the longest increasing subsequence with the maximum sum.

        Args:
            nums: A list of integers.

        Returns:
            The sum of the longest increasing subsequence with the maximum sum.
        """

        n = len(nums)
        # dp[i] stores the sum of the longest increasing subsequence ending at index i.
        dp = [0] * n
        # Initialize dp with the value of the element itself, as a single element is an increasing subsequence.
        for i in range(n):
            dp[i] = nums[i]

        # Iterate through the array and update dp values.
        for i in range(1, n):
            for j in range(i):
                # If the current element is greater than the previous element,
                # we can extend the increasing subsequence ending at index j.
                if nums[i] > nums[j]:
                    # Update dp[i] if extending the subsequence ending at index j
                    # results in a larger sum.
                    dp[i] = max(dp[i], dp[j] + nums[i])

        # The maximum value in dp is the sum of the longest increasing subsequence with the maximum sum.
        return max(dp)

    return longest_increasing_subsequence_with_max_sum

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    nums1 = [1, 101, 2, 3, 100, 4, 5]
    expected1 = 106
    assert func(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(nums1)}"

    # Test case 2
    nums2 = [10, 5, 4, 3]
    expected2 = 10
    assert func(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(nums2)}"

    # Test case 3
    nums3 = [1, 3, 2, 4, 5]
    expected3 = 15
    assert func(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(nums3)}"

    # Test case 4
    nums4 = [4, 2, 3, 10, 1, 5, 6]
    expected4 = 21
    assert func(nums4) == 21, f"Test Case 4 Failed: Expected {21}, Got {func(nums4)}"

    # Test case 5: Empty list
    nums5 = []
    expected5 = 0  # Define what should happen with empty lists
    assert func(nums5) == 0, f"Test Case 5 Failed: Expected {0}, Got {func(nums5)}"

    # Test case 6: List with one element
    nums6 = [5]
    expected6 = 5
    assert func(nums6) == 5, f"Test Case 6 Failed: Expected {5}, Got {func(nums6)}"
    
    # Test case 7: Decreasing list
    nums7 = [5,4,3,2,1]
    expected7 = 5
    assert func(nums7) == 5, f"Test Case 7 Failed: Expected {5}, Got {func(nums7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()