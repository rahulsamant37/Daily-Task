# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) with a twist. The twist is that you can only consider an element `nums[i]` to be part of the increasing subsequence if `nums[i]` is divisible by the previous element in the subsequence.

For example:
Input: nums = [1, 3, 6, 12, 24, 36]
Output: 6
Explanation: [1, 3, 6, 12, 24, 36] is the longest increasing subsequence where each element is divisible by the previous one.

Input: nums = [1, 2, 3, 4, 5, 6]
Output: 3
Explanation: One possible longest increasing subsequence is [1, 2, 4]. The length is 3.

Input: nums = [4, 8, 10, 240]
Output: 3
Explanation: One possible longest increasing subsequence is [4, 8, 240]. The length is 3.

'''

# Solution
def solution():
    def longest_divisible_subsequence(nums):
        """
        Finds the length of the longest increasing subsequence where each element is divisible by the previous one.

        Args:
          nums: A list of integers.

        Returns:
          The length of the longest divisible subsequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest divisible subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array
        for i in range(1, n):
            # For each element, iterate through all previous elements
            for j in range(i):
                # If the current element is divisible by the previous element
                if nums[i] % nums[j] == 0:
                    # Update the length of the longest divisible subsequence ending at nums[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum length among all dp values
        return max(dp)

    return longest_divisible_subsequence

# Test cases
def test_solution():
    longest_divisible_subsequence = solution()

    # Test case 1
    nums1 = [1, 3, 6, 12, 24, 36]
    expected1 = 6
    assert longest_divisible_subsequence(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_divisible_subsequence(nums1)}"

    # Test case 2
    nums2 = [1, 2, 3, 4, 5, 6]
    expected2 = 3
    assert longest_divisible_subsequence(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_divisible_subsequence(nums2)}"

    # Test case 3
    nums3 = [4, 8, 10, 240]
    expected3 = 3
    assert longest_divisible_subsequence(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_divisible_subsequence(nums3)}"

    # Test case 4
    nums4 = [2, 3, 4, 5, 6, 7, 8]
    expected4 = 3
    assert longest_divisible_subsequence(nums4) == 3, f"Test Case 4 Failed: Expected {3}, got {longest_divisible_subsequence(nums4)}"

    # Test case 5: Empty list
    nums5 = []
    expected5 = 0
    assert longest_divisible_subsequence(nums5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_divisible_subsequence(nums5)}"

    # Test case 6: Single element
    nums6 = [5]
    expected6 = 1
    assert longest_divisible_subsequence(nums6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_divisible_subsequence(nums6)}"
    
    # Test case 7: All same elements
    nums7 = [2, 2, 2, 2]
    expected7 = 1
    assert longest_divisible_subsequence(nums7) == 1, f"Test Case 7 Failed: Expected {expected7}, got {longest_divisible_subsequence(nums7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()