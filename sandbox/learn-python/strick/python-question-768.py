# Python Question: Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of the elements in the LIS is maximized. Return the maximum sum.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106  (The LIS is [1, 2, 3, 100], and its sum is 106)

Input: nums = [10, 5, 4, 3, 2, 1]
Output: 10  (The LIS is [10], and its sum is 10)

Input: nums = [1, 3, 2, 4, 5]
Output: 15 (The LIS is [1, 2, 4, 5] and its sum is 12 or [1,3,4,5] and its sum is 13 or [1,2,4,5] and its sum is 12 or [1,3,4,5] and its sum is 13. The correct LIS is [1,3,4,5] and its sum is 13.
Another possible LIS is [1,3,5] with a sum of 9.
Or [1,2,4,5], which has a sum of 12.
The LIS is [1,3,4,5], which has a sum of 13.  However, let us test with the testcase [1, 101, 2, 3, 100, 4, 5].
LIS is [1,2,3,4,5] sum is 15
LIS is [1,2,3,100] sum is 106
LIS is [1,2,100] sum is 103
LIS is [1,2,3,4] sum is 10
LIS is [1,2,3,5] sum is 11
LIS is [1,101] sum is 102
LIS is [1,100] sum is 101
LIS is [1,101] sum is 102
LIS is [1,100] sum is 101
LIS is [1,101] sum is 102
LIS is [1,2,3,100] sum is 106

'''

# Solution
def solution(nums):
    """
    Finds the longest increasing subsequence with the maximum sum.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of the LIS.
    """
    n = len(nums)
    # dp[i] stores the maximum sum of an increasing subsequence ending at nums[i]
    dp = [0] * n

    # Initialize dp with the values of nums themselves, as each element can be a subsequence of length 1
    for i in range(n):
        dp[i] = nums[i]

    # Iterate through the array to find longer increasing subsequences
    for i in range(1, n):
        for j in range(i):
            # If nums[i] can extend the increasing subsequence ending at nums[j]
            if nums[i] > nums[j]:
                # Update dp[i] if including nums[i] improves the maximum sum
                dp[i] = max(dp[i], dp[j] + nums[i])

    # The maximum value in dp represents the maximum sum of any increasing subsequence
    return max(dp) if dp else 0

# Test cases
def test_solution():
    assert solution([1, 101, 2, 3, 100, 4, 5]) == 106
    assert solution([10, 5, 4, 3, 2, 1]) == 10
    assert solution([1, 3, 2, 4, 5]) == 15
    assert solution([1, 5, 2, 4, 3]) == 11
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([5,4,3,2,1]) == 5
    assert solution([1,2,3,4,5]) == 15
    assert solution([1,2,3]) == 6
    assert solution([3,2,1]) == 3
    assert solution([4,2,4,5,3,7]) == 16
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()