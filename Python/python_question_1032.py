# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) with the following constraint:
For any two consecutive elements `nums[i]` and `nums[j]` in the subsequence (where `i < j`), `nums[j] - nums[i] >= k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 3
Explanation: The longest increasing subsequence satisfying the constraint is [3, 10, 20]. Its length is 3. Another possible LIS is [1,20] with length 2.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 2
Explanation: Possible LIS with the constraint are [1, 5], [1, 4], [2, 4], [3]. Note that [1, 2, 3] or [1, 2, 4] are increasing but do not satisfy the condition element[j] - element[i] >=k for consecutive elements.

'''

# Solution
def longest_increasing_subsequence_with_k(nums, k):
    """
    Finds the length of the longest increasing subsequence in nums with the given constraint.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum difference between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through each element in the array
    for i in range(1, n):
        # For each element, iterate through all previous elements
        for j in range(i):
            # Check if nums[i] > nums[j] (increasing subsequence) and nums[i] - nums[j] >= k (constraint)
            if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                # If both conditions are met, update dp[i] to be the maximum of its current value and dp[j] + 1
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp array is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_k([3, 10, 2, 1, 20], 3) == 3
    assert longest_increasing_subsequence_with_k([1, 5, 2, 4, 3], 2) == 2
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 2) == 1
    assert longest_increasing_subsequence_with_k([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_k([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_k([1, 3, 5, 2, 4, 6], 2) == 3
    assert longest_increasing_subsequence_with_k([1, 3, 5, 2, 4, 6], 3) == 2
    assert longest_increasing_subsequence_with_k([], 3) == 0
    assert longest_increasing_subsequence_with_k([1], 3) == 1
    assert longest_increasing_subsequence_with_k([1,4], 3) == 2
    assert longest_increasing_subsequence_with_k([1,2,3,4], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()