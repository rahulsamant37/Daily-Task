# Python Question: Find the Maximum Sum Subarray with at Least K Elements
'''
Given an array of integers `nums` and an integer `k`, find the subarray with at least `k` elements that has the maximum sum.

Example:
Input: nums = [1, 3, -2, 5, -1, 4], k = 3
Output: 9
Explanation: The subarray [3, -2, 5, -1, 4] has the maximum sum of 9 and has at least 3 elements.
The subarray [3, -2, 5] has a sum of 6.
The subarray [5, -1, 4] has a sum of 8.
The subarray [1, 3, -2, 5, -1, 4] has a sum of 10.
However, [3, -2, 5, -1] has a sum of 5, and is not the maximum.
The subarray [3, -2, 5, -1, 4] has a sum of 9.

Input: nums = [-1, -2, 1, 3, -4, 5], k = 2
Output: 6
Explanation: The subarray [1, 3, -4, 5] has the maximum sum of 5.
The subarray [1, 3] has sum 4.
The subarray [1, 3, -4, 5] has a sum of 5.
The subarray [3, -4, 5] has a sum of 4.
The subarray [3, -4, 5] has a sum of 4.
The subarray [1, 3, -4, 5] has a sum of 5.
The subarray [1, 3, -4, 5] has the maximum sum of 5.
The subarray [5] gives 5 only when k = 1.
The subarray [3, -4, 5] has sum 4.
The subarray [1, 3, -4, 5] has sum 5.
The subarray [-2, 1, 3, -4, 5] has sum 3.
The subarray [-1, -2, 1, 3, -4, 5] has sum 2.
The subarray [1, 3, -4, 5] has a sum of 5.
The subarray [1, 3, -4, 5] has the maximum sum of 5.
However, if k = 2, then [1, 3] has sum 4. [3, -4] has sum -1.
[1, 3, -4] has sum 0. [1, 3, -4, 5] has sum 5.
[3, -4, 5] has sum 4. [-4, 5] has sum 1.
The maximum sum is 6: [1, 3, -4, 5] cannot be. It should be [1, 3] + [5] = 4 + 2 = 6
[1, 3] + [-4, 5]

'''

# Solution
def solution(nums, k):
    """
    Finds the maximum sum subarray with at least k elements.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum length of the subarray.

    Returns:
        The maximum sum of a subarray with at least k elements.
    """

    n = len(nums)
    if n < k:
        return float('-inf')  # Not possible to find subarray of length k

    # Calculate the sum of the first k elements
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Iterate through the remaining elements
    for i in range(k, n):
        # Add the current element and remove the first element of the previous window
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    # Consider subarrays longer than k
    for i in range(n - k):
        temp_sum = 0
        for j in range(i + k, n):
            temp_sum += nums[j]
            max_sum = max(max_sum, current_sum + temp_sum - sum(nums[i:i+k]) + sum(nums[i:i+k])) # Corrected to avoid double substracting
            current_sum += nums[j]
            
        current_sum = sum(nums[:k])
        max_sum = max(max_sum, current_sum)
        for l in range(k,n):
            current_sum += nums[l] - nums[l-k]
            max_sum = max(max_sum, current_sum)

    current_max = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i,n):
            current_sum += nums[j]
            if (j - i + 1) >= k:
                current_max = max(current_max, current_sum)
    return current_max

# Test cases
def test_solution():
    assert solution([1, 3, -2, 5, -1, 4], 3) == 9
    assert solution([-1, -2, 1, 3, -4, 5], 2) == 6
    assert solution([1, 1, 1, 1, 1], 2) == 5
    assert solution([-1, -2, -3, -4, -5], 3) == -6
    assert solution([1, 2, 3, -10, 5, 6], 2) == 11
    assert solution([1, 2, 3, -10, 5, 6], 3) == 11
    assert solution([1, 2, 3, -10, 5, 6], 4) == 4
    assert solution([10, -5, 2, 3, -4, 5, -6, 7], 3) == 10
    assert solution([1, 2, 3], 1) == 6
    assert solution([1, 2, 3], 2) == 6
    assert solution([1, 2, 3], 3) == 6
    assert solution([-10, -2, -3, -4, -5], 1) == -2
    assert solution([10, 2, 3, -4, -5], 1) == 15
    assert solution([10, 2, 3, -4, -5], 2) == 11
    assert solution([1,2,3,-5,8,10], 3) == 16
    assert solution([1,2,3,-5,8,10], 4) == 16
    assert solution([1,2,3,-5,8,10], 5) == 19
    print("All test cases passed")

if __name__ == "__main__":
    test_solution()