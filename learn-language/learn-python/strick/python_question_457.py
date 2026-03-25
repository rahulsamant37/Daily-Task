# Python Question: Longest Increasing Subsequence with Minimum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of the elements in the LIS is minimized. If there are multiple LIS with the same length, return the one with the minimum sum.

Example:
Input: [1, 3, 2, 4, 5]
Output: [1, 2, 4, 5]

Input: [1, 3, 2, 4, 5, 0]
Output: [1, 2, 4, 5]

Input: [5, 2, 8, 6, 3, 6, 9, 5]
Output: [2, 3, 6, 9]

Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: [10, 22, 33, 41, 60, 80]
'''

# Solution
def longest_increasing_subsequence_with_minimum_sum(arr):
    """
    Finds the longest increasing subsequence (LIS) with the minimum sum.

    Args:
        arr: A list of integers.

    Returns:
        A list of integers representing the LIS with the minimum sum.
    """

    n = len(arr)
    if n == 0:
        return []

    # dp[i] stores the length of the LIS ending at arr[i]
    dp = [1] * n
    # sum_dp[i] stores the sum of the LIS ending at arr[i]
    sum_dp = [arr[i] for i in range(n)]
    # prev[i] stores the index of the previous element in the LIS ending at arr[i]
    prev = [i] * n

    # Iterate through the array to build the dp and sum_dp arrays
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                # If we can extend the LIS ending at arr[j] with arr[i]
                if dp[j] + 1 > dp[i]:
                    # If the new LIS is longer, update dp[i], sum_dp[i], and prev[i]
                    dp[i] = dp[j] + 1
                    sum_dp[i] = sum_dp[j] + arr[i]
                    prev[i] = j
                elif dp[j] + 1 == dp[i] and sum_dp[j] + arr[i] < sum_dp[i]:
                    # If the new LIS has the same length but a smaller sum, update sum_dp[i] and prev[i]
                    sum_dp[i] = sum_dp[j] + arr[i]
                    prev[i] = j

    # Find the index of the LIS with the maximum length and minimum sum
    max_len = max(dp)
    indices = [i for i, val in enumerate(dp) if val == max_len]
    best_index = indices[0]
    for index in indices:
        if sum_dp[index] < sum_dp[best_index]:
            best_index = index

    # Reconstruct the LIS from the prev array
    lis = []
    curr = best_index
    while curr != prev[curr]:
        lis.append(arr[curr])
        curr = prev[curr]
    lis.append(arr[curr])

    return lis[::-1]  # Reverse the list to get the correct order


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_minimum_sum([1, 3, 2, 4, 5]) == [1, 2, 4, 5]
    assert longest_increasing_subsequence_with_minimum_sum([1, 3, 2, 4, 5, 0]) == [1, 2, 4, 5]
    assert longest_increasing_subsequence_with_minimum_sum([5, 2, 8, 6, 3, 6, 9, 5]) == [2, 3, 6, 9]
    assert longest_increasing_subsequence_with_minimum_sum([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 41, 60, 80]
    assert longest_increasing_subsequence_with_minimum_sum([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence_with_minimum_sum([5, 4, 3, 2, 1]) == [5]
    assert longest_increasing_subsequence_with_minimum_sum([1, 1, 1, 1, 1]) == [1]
    assert longest_increasing_subsequence_with_minimum_sum([]) == []
    assert longest_increasing_subsequence_with_minimum_sum([1]) == [1]
    assert longest_increasing_subsequence_with_minimum_sum([3,10,2,1,20]) == [3, 10, 20]
    assert longest_increasing_subsequence_with_minimum_sum([4,1,2,3,4,4,5]) == [1, 2, 3, 4, 5]

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()