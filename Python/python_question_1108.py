# Python Question: Find the Longest Increasing Subsequence with Specific Property
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is a prime number.

Example:
Input: nums = [1, 2, 3, 5, 6, 8, 11, 12]
Output: 5
Explanation: The longest increasing subsequence with prime difference is [1, 2, 3, 5, 11], where the differences are [1, 1, 2, 6].
However, [1, 2, 3, 5, 6, 8, 11] has differences [1, 1, 2, 1, 2, 3].
[1, 2, 3, 5, 11] has differences [1, 1, 2, 6]. Only [2,3,5,11] is valid, with the differences [1,2,6].
The correct longest increasing subsequence is [2,3,5,11,12], where differences are [1,2,6,1].
The prime differences are [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]. 1 is not prime.
Prime differences are [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97].
The longest increasing subsequence with prime differences is [2, 3, 5, 11], with differences [1,2,6] and length 4. This is incorrect.
The longest increasing subsequence with prime differences [2, 3, 5] has length 3.
The longest increasing subsequence with prime differences [2, 3, 5, 11] has length 4.
The longest increasing subsequence with prime differences [2, 3, 5, 6] is not valid.
The longest increasing subsequence with prime differences [1, 2, 3, 5] is not valid.
The longest increasing subsequence with prime differences [2, 3, 5, 11] has length 4.
The longest increasing subsequence with prime differences [2, 5, 11] has length 3.
The longest increasing subsequence with prime differences [3, 5, 11] has length 3.
The longest increasing subsequence with prime differences [5, 11] has length 2.
The longest increasing subsequence with prime differences [11] has length 1.
The longest increasing subsequence with prime differences [1, 2, 3, 5, 6, 8, 11, 12] is [2, 3, 5] with length 3.
The longest increasing subsequence with prime differences [1, 2, 3, 5, 8, 11] is [2,3,5] with length 3.
'''

# Solution
def solution():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def longest_increasing_subsequence_prime_diff(nums):
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

    return longest_increasing_subsequence_prime_diff(nums)

# Test cases
def test_solution():
    nums1 = [1, 2, 3, 5, 6, 8, 11, 12]
    nums2 = [1, 3, 7, 12, 19]
    nums3 = [2, 3, 5, 7, 11]
    nums4 = [1, 4, 6, 8, 10, 12]
    nums5 = []
    nums6 = [2]
    nums7 = [1, 2, 4, 7]
    nums8 = [2, 4, 6, 8]
    nums9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    nums10 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    print(f"Test Case 1: {nums1}, Output: {solution()}") # Expected output: 4
    nums = nums1
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def longest_increasing_subsequence_prime_diff(nums):
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
    assert longest_increasing_subsequence_prime_diff(nums1) == 4

    print(f"Test Case 2: {nums2}, Output: {solution()}") # Expected output: 4
    assert longest_increasing_subsequence_prime_diff(nums2) == 4
    print(f"Test Case 3: {nums3}, Output: {solution()}") # Expected output: 5
    assert longest_increasing_subsequence_prime_diff(nums3) == 5
    print(f"Test Case 4: {nums4}, Output: {solution()}") # Expected output: 1
    assert longest_increasing_subsequence_prime_diff(nums4) == 1
    print(f"Test Case 5: {nums5}, Output: {solution()}") # Expected output: 0
    assert longest_increasing_subsequence_prime_diff(nums5) == 0
    print(f"Test Case 6: {nums6}, Output: {solution()}") # Expected output: 1
    assert longest_increasing_subsequence_prime_diff(nums6) == 1
    print(f"Test Case 7: {nums7}, Output: {solution()}") # Expected output: 3
    assert longest_increasing_subsequence_prime_diff(nums7) == 3
    print(f"Test Case 8: {nums8}, Output: {solution()}") # Expected output: 1
    assert longest_increasing_subsequence_prime_diff(nums8) == 1
    print(f"Test Case 9: {nums9}, Output: {solution()}") # Expected output: 4
    assert longest_increasing_subsequence_prime_diff(nums9) == 4
    print(f"Test Case 10: {nums10}, Output: {solution()}") # Expected output: 11
    assert longest_increasing_subsequence_prime_diff(nums10) == 11


if __name__ == "__main__":
    test_solution()