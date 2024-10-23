# Python Question: Maximum Subarray Sum with at Most K Distinct Elements
'''
Given an array of integers `nums` and an integer `k`, find the maximum sum of any subarray of `nums` that contains at most `k` distinct elements.

Example:
Input: nums = [1, 2, 1, 3, 4, 2, 5], k = 3
Output: 12
Explanation: The subarray [1, 3, 4, 2] has at most 3 distinct elements (1, 3, 4, 2) and has the maximum sum of 1 + 3 + 4 + 2 = 10.
The subarray [3, 4, 2, 5] has at most 3 distinct elements (3, 4, 2, 5) and has a sum of 3 + 4 + 2 + 5 = 14. However, subarray [4,2,5] has at most 3 distinct elements (4,2,5) and has a sum of 4+2+5 = 11, and subarray [2,5] has at most 2 distinct elements (2,5) and has a sum of 2+5 = 7.
The subarray [1, 2, 1, 3, 4] has at most 4 distinct elements (1,2,3,4) and has a sum of 1+2+1+3+4 = 11.
The subarray [1, 2, 1, 3] has at most 3 distinct elements (1,2,3) and has a sum of 1+2+1+3 = 7.
The subarray [2, 1, 3, 4] has at most 4 distinct elements (2,1,3,4) and has a sum of 2+1+3+4 = 10.
The subarray [1, 2, 1, 3, 4, 2] has at most 4 distinct elements (1,2,3,4) and has a sum of 1+2+1+3+4+2 = 13.
The subarray [1, 2, 1, 3, 4, 2, 5] has at most 5 distinct elements (1,2,3,4,5) and has a sum of 1+2+1+3+4+2+5 = 18.
The subarray [3, 4, 2, 5] has at most 4 distinct elements (3,4,2,5) and has a sum of 3 + 4 + 2 + 5 = 14. The subarray [4,2,5] has at most 3 distinct elements (4,2,5) and has a sum of 4 + 2 + 5 = 11.
The subarray [1, 2, 1, 3] has at most 3 distinct elements (1, 2, 3) and has a sum of 7.

'''

# Solution
def solution(nums, k):
    """
    Finds the maximum sum of any subarray of nums that contains at most k distinct elements.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum number of distinct elements allowed in the subarray.

    Returns:
        The maximum sum of any subarray of nums that contains at most k distinct elements.
    """

    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarray = nums[i:j+1]
            distinct_elements = len(set(subarray))
            if distinct_elements <= k:
                current_sum = sum(subarray)
                max_sum = max(max_sum, current_sum)
    return max_sum

# Solution using sliding window
def solution_sliding_window(nums, k):
    """
    Finds the maximum sum of any subarray of nums that contains at most k distinct elements using sliding window.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum number of distinct elements allowed in the subarray.

    Returns:
        The maximum sum of any subarray of nums that contains at most k distinct elements.
    """

    max_sum = 0
    window_start = 0
    window_sum = 0
    freq_map = {}

    for window_end in range(len(nums)):
        right_num = nums[window_end]
        if right_num not in freq_map:
            freq_map[right_num] = 0
        freq_map[right_num] += 1
        window_sum += right_num

        while len(freq_map) > k:
            left_num = nums[window_start]
            freq_map[left_num] -= 1
            if freq_map[left_num] == 0:
                del freq_map[left_num]
            window_sum -= nums[window_start]
            window_start += 1

        max_sum = max(max_sum, window_sum)

    return max_sum

# Test cases
def test_solution():
    assert solution_sliding_window([1, 2, 1, 3, 4, 2, 5], 3) == 14
    assert solution_sliding_window([1, 2, 1, 3, 4, 2, 5], 2) == 7
    assert solution_sliding_window([1, 2, 3, 4, 5], 1) == 5
    assert solution_sliding_window([1, 2, 3, 4, 5], 5) == 15
    assert solution_sliding_window([1, 1, 1, 1, 1], 1) == 5
    assert solution_sliding_window([1, 2, 1, 3, 4, 2, 5], 4) == 18
    assert solution_sliding_window([1, 2, 1, 3, 4, 2, 5], 5) == 18
    assert solution_sliding_window([1], 1) == 1
    assert solution_sliding_window([], 1) == 0
    assert solution_sliding_window([1,2,3,4,5,6,7,8,9,10], 3) == 24
    assert solution_sliding_window([2,1,3,5,4,2,1], 3) == 15
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()