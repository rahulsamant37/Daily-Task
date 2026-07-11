# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 5
Output: 4
Explanation: The longest increasing subsequence with difference at most 5 is [3, 2, 1, 20] or [3, 10, 20].  The length is 3. Another possible LIS is [1, 2, 3, 10, 20] but this contains [1,2,3,10] where the difference is 7 between 3 and 10. The length of the LIS is 3.  However, [2,3,10,20] with length 4 is also acceptable. Consider the subsequence [1, 2, 3, 10, 20].  The difference between 1 and 2 is 1 <= 5.  The difference between 2 and 3 is 1 <= 5. The difference between 3 and 10 is 7 which is > 5. The difference between 10 and 20 is 10 which is > 5. Thus, this subsequence is invalid. A valid subsequence is [1,2,3]. Another valid subsequence is [2,3,10]. The length is 3. The valid subsequence [3,10,20] has a length of 3. Another one is [1,2,20] which is invalid because 1 < 2 < 20 is not increasing, 1 <= 2 <= 20.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with difference at most 2 is [1, 2, 3] or [1, 2, 4] or [1, 3, 4] or [2, 3, 4] or [1,4]. The length is 3.

Input: nums = [1, 2, 3, 4, 5], k = 1
Output: 2
Explanation: The longest increasing subsequence with difference at most 1 is [1, 2], [2, 3], [3, 4], or [4, 5]. The length is 2. The subsequence [1,2,3,4,5] is invalid since 2-1 <= 1, 3-2 <= 1, 4-3 <= 1, and 5-4 <= 1, and the difference is 1, so the entire subsequence should be included, and the length should be 5.

Input: nums = [1, 2, 3, 4, 5], k = 0
Output: 1
Explanation: The longest increasing subsequence with difference at most 0 is [1], [2], [3], [4], or [5]. The length is 1.

Input: nums = [1, 10, 2, 20, 3, 30], k = 5
Output: 4
Explanation: The longest increasing subsequence with a difference at most 5 is [1, 2, 3, 30] or [1, 2, 3]. The length is 3. Another valid option is [1,2,3,10] which is not valid since 10-3 > 5. The solution [1,2,3] has a length of 3. The solution [2,3] has a length of 2. [1,2,3,10,20,30] is invalid.
[1,2,3] is valid.
[1,2,3,30] is invalid: 30-3 > 5.
[1,2,10,20,30] is invalid: 10-2 > 5.
[10,20,30] is valid.
[2,3] is valid.
[2,20] is invalid.
[3,30] is valid.
[1,2,3] has length 3.
[10,20,30] has length 3.
[2,3] has length 2.
[3,30] has length 2.
The maximum length is 3. [1,2,3], [10,20,30]

'''

# Solution
def longest_increasing_subsequence_with_difference(nums, k):
    """
    Finds the length of the longest increasing subsequence with a difference at most k.

    Args:
        nums: A list of integers.
        k: The maximum difference allowed between consecutive elements.

    Returns:
        The length of the longest increasing subsequence.
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    # Iterate through the array
    for i in range(1, n):
        # For each element, iterate through all previous elements
        for j in range(i):
            # If the current element is greater than the previous element
            # and the difference between them is at most k,
            # then update the length of the longest increasing subsequence ending at the current element
            if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in dp is the length of the longest increasing subsequence
    return max(dp)

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_difference([3, 10, 2, 1, 20], 5) == 3
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 4, 3], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 1) == 2
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 10, 2, 20, 3, 30], 5) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5], 5) == 5
    assert longest_increasing_subsequence_with_difference([5, 4, 3, 2, 1], 1) == 1
    assert longest_increasing_subsequence_with_difference([1, 5, 2, 4, 3, 6, 7, 8], 3) == 4
    assert longest_increasing_subsequence_with_difference([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 2
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == 1
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == 3
    assert longest_increasing_subsequence_with_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == 4
    assert longest_increasing_subsequence_with_difference([], 5) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()