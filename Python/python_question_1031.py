# Python Question: Longest Increasing Subsequence with Minimum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of elements in the LIS is minimized. If there are multiple LIS with the same length, return the one with the minimum sum.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: [1, 2, 4, 5]

Input: nums = [1, 3, 2, 4, 5, 1, 2, 3]
Output: [1, 2, 3]

Input: nums = [5, 4, 3, 2, 1]
Output: [1]

Input: nums = [1, 5, 2, 4, 3]
Output: [1, 2, 3]
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_min_sum(nums):
        """
        Finds the longest increasing subsequence (LIS) with the minimum sum.

        Args:
            nums: A list of integers.

        Returns:
            A list representing the LIS with the minimum sum.
        """
        n = len(nums)
        if n == 0:
            return []

        # dp[i] stores the length of the LIS ending at nums[i]
        dp = [1] * n
        # sum_dp[i] stores the sum of the LIS ending at nums[i]
        sum_dp = [num for num in nums]
        # prev[i] stores the index of the previous element in the LIS ending at nums[i]
        prev = [i] * n

        # Iterate through the array to build the dp and sum_dp arrays
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If extending the LIS ending at nums[j] with nums[i] results in a longer LIS
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        sum_dp[i] = sum_dp[j] + nums[i]
                        prev[i] = j
                    # If the LIS length is the same, choose the one with the minimum sum
                    elif dp[i] == dp[j] + 1 and sum_dp[i] > sum_dp[j] + nums[i]:
                        sum_dp[i] = sum_dp[j] + nums[i]
                        prev[i] = j

        # Find the index of the maximum length LIS
        max_len = max(dp)
        indices = [i for i, val in enumerate(dp) if val == max_len]

        # Among the LIS with the maximum length, find the one with the minimum sum
        min_sum = float('inf')
        end_index = -1
        for index in indices:
            if sum_dp[index] < min_sum:
                min_sum = sum_dp[index]
                end_index = index

        # Reconstruct the LIS from the end index using the prev array
        lis = []
        curr = end_index
        while curr != prev[curr]:
            lis.append(nums[curr])
            curr = prev[curr]
        lis.append(nums[curr])

        return sorted(lis)

    return longest_increasing_subsequence_with_min_sum
    

# Test cases
def test_solution():
    longest_increasing_subsequence_with_min_sum = solution()
    assert longest_increasing_subsequence_with_min_sum([1, 3, 2, 4, 5]) == [1, 2, 4, 5]
    assert longest_increasing_subsequence_with_min_sum([1, 3, 2, 4, 5, 1, 2, 3]) == [1, 2, 3]
    assert longest_increasing_subsequence_with_min_sum([5, 4, 3, 2, 1]) == [1]
    assert longest_increasing_subsequence_with_min_sum([1, 5, 2, 4, 3]) == [1, 2, 3]
    assert longest_increasing_subsequence_with_min_sum([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 21, 41, 60, 80]
    assert longest_increasing_subsequence_with_min_sum([3, 10, 2, 1, 20]) == [1, 2, 20]
    assert longest_increasing_subsequence_with_min_sum([]) == []
    assert longest_increasing_subsequence_with_min_sum([1]) == [1]
    assert longest_increasing_subsequence_with_min_sum([1, 1, 1, 1]) == [1]
    assert longest_increasing_subsequence_with_min_sum([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()