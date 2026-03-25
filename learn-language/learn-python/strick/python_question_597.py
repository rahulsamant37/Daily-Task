# Python Question: Maximum Subarray Sum After One Operation
'''
Given an array of integers `nums`, you are allowed to perform one operation: choose any element `nums[i]` and multiply it by `x`. You can choose to perform this operation at most once. Your task is to find the maximum possible sum of a contiguous subarray in `nums` after performing this operation (or not performing it at all).

Example:
Input: nums = [2, -1, -4, 5], x = 2
Output: 11
Explanation: We can choose to multiply nums[2] by 2, so the array becomes [2, -1, -8, 5]. The maximum subarray sum is 5 (from index 3 to 3).
However, if we multiply nums[3] by 2, the array becomes [2, -1, -4, 10]. The maximum subarray sum is 11 (from index 0 to 3).

Input: nums = [1, -1, 2, -2, 3], x = 3
Output: 9
Explanation: We can multiply nums[4] by 3, making the array [1, -1, 2, -2, 9]. The maximum subarray sum is 9.
'''

# Solution
def solution():
    def max_subarray_sum(nums):
        """
        Calculates the maximum subarray sum using Kadane's Algorithm.
        """
        max_so_far = float('-inf')
        current_max = 0
        for i in range(len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    def solve(nums, x):
        """
        Finds the maximum subarray sum after applying the multiplication operation at most once.
        """
        n = len(nums)
        max_sum = max_subarray_sum(nums)  # Initial max sum without multiplication

        for i in range(n):
            original_value = nums[i]
            nums[i] *= x  # Multiply nums[i] by x
            max_sum = max(max_sum, max_subarray_sum(nums))  # Update max_sum if necessary
            nums[i] = original_value  # Revert back to the original value for the next iteration

        return max_sum

    return solve
    
# Test cases
def test_solution():
    solve = solution()
    assert solve([2, -1, -4, 5], 2) == 11
    assert solve([1, -1, 2, -2, 3], 3) == 9
    assert solve([-1, -2], 2) == -1
    assert solve([1, 2, 3], 2) == 12
    assert solve([-2, 5, -1, 4], 2) == 15
    assert solve([-2, -3, 4, -1, -2, 1, 5, -3], 2) == 13
    assert solve([1, -2, 0, 3], 4) == 12
    assert solve([1, -1, -2, 4, -1], 3) == 12
    assert solve([-5, -2, 0, 5, 2], 2) == 14

if __name__ == "__main__":
    test_solution()