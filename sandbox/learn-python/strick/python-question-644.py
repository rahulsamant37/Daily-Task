# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence such that the difference between adjacent elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 3, 4] or [2, 3, 4, 5], both with length 4. Note that [1, 3, 4, 5] is not valid because the difference between 1 and 3 is greater than k=1.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 3], [1, 2, 4], or [2, 3, 4], all with length 3.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_diff(nums, k):
        """
        Finds the length of the longest increasing subsequence in nums with a maximum difference of k between adjacent elements.

        Args:
            nums: A list of integers.
            k: The maximum difference allowed between adjacent elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] can extend the subsequence ending at nums[j]
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_with_k_diff

# Test cases
def test_solution():
    nums1 = [1, 3, 2, 4, 5]
    k1 = 1
    expected1 = 4
    assert solution()(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {solution()(nums1, k1)}"

    nums2 = [1, 5, 2, 4, 3]
    k2 = 2
    expected2 = 3
    assert solution()(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {solution()(nums2, k2)}"

    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    expected3 = 1
    assert solution()(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {solution()(nums3, k3)}"

    nums4 = [5, 4, 3, 2, 1]
    k4 = 1
    expected4 = 1
    assert solution()(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {solution()(nums4, k4)}"

    nums5 = [1, 1, 1, 1, 1]
    k5 = 0
    expected5 = 1
    assert solution()(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {solution()(nums5, k5)}"

    nums6 = [1, 2, 3, 4, 5]
    k6 = 5
    expected6 = 5
    assert solution()(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {solution()(nums6, k6)}"

    nums7 = []
    k7 = 1
    expected7 = 0
    assert solution()(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {solution()(nums7, k7)}"

    nums8 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k8 = 10
    expected8 = 6
    assert solution()(nums8, k8) == 6, f"Test Case 8 Failed: Expected {6}, got {solution()(nums8, k8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()