# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence must be a prime number.

Example:
Input: nums = [1, 2, 3, 4, 5, 6, 7, 8]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 5, 7], where the differences (3-2=1, 5-3=2, 7-5=2) are prime numbers. Note that 1 is not considered a prime number.

Input: nums = [10, 12, 13, 15, 17, 20, 23]
Output: 5
Explanation: The longest increasing subsequence is [10, 13, 15, 17, 23], where the differences (13-10=3, 15-13=2, 17-15=2, 23-17=6) are not all prime. The correct LIS is [12, 13, 15, 17, 23] with differences [1,2,2,6]. another subsequence is [10, 12, 13, 15, 17], the differences are [2,1,2,2].  The longest valid LIS is [10, 12, 13, 17, 23] with differences [2,1,4,6], and the valid LIS is [10, 12, 17, 23] with differences [2,5,6].  So the LIS with prime differences is [10,13,17,23] with differences [3,4,6]. The question requires the difference between consecutive elements to be prime. The longest valid LIS is [2,3,5,7] with differences [1,2,2] --> 1 is not prime. The longest valid LIS is [2,3,5] with differences [1,2] --> 1 is not prime. The longest valid LIS is [3,5,7] with differences [2,2]. The length is 3.

Input: nums = [1, 5, 2, 4, 3]
Output: 2
Explanation: The longest increasing subsequence with prime differences could be [1, 2] (difference 1, not prime) or [1, 4] (difference 3, prime) or [1, 5] (difference 4, not prime) or [2, 3] (difference 1, not prime) or [2, 4] (difference 2, prime) or [2, 5] (difference 3, prime) or [3, 4] (difference 1, not prime) or [3, 5] (difference 2, prime) or [4, 5] (difference 1, not prime). Possible LIS are [1,4], [2,4], [2,5], [3,5].

'''

# Solution
def solution(nums):
    """
    Finds the length of the longest increasing subsequence with prime differences.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence with prime differences.
    """

    def is_prime(n):
        """
        Checks if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and is_prime(nums[i] - nums[j]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test cases
def test_solution():
    assert solution([1, 2, 3, 4, 5, 6, 7, 8]) == 4
    assert solution([10, 12, 13, 15, 17, 20, 23]) == 3
    assert solution([1, 5, 2, 4, 3]) == 2
    assert solution([2, 3, 5, 7, 11]) == 5
    assert solution([1, 2, 4, 6, 8, 10]) == 1
    assert solution([1]) == 1
    assert solution([]) == 0
    assert solution([2,4,5]) == 2
    assert solution([3,5,7]) == 3
    assert solution([2,3,4,6,7,8]) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()