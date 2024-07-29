# Python Question: Largest Sum Contiguous Subarray
'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Solution
def solution():
    def maxSubArray(nums):
        """
        Kadane's Algorithm:
        This algorithm efficiently finds the maximum sum of a contiguous subarray within a given array.

        The core idea is to maintain two variables:
        - `max_so_far`: Stores the maximum sum encountered so far. Initialized to negative infinity to handle cases where all numbers are negative.
        - `current_max`: Stores the maximum sum ending at the current position. Initialized to 0.

        Iterate through the array:
        1. Update `current_max` by adding the current element.
        2. If `current_max` becomes negative, reset it to 0, as a negative sum ending at the current position would only decrease the sum of any subsequent subarray.
        3. Update `max_so_far` with the maximum of `max_so_far` and `current_max`.

        Return `max_so_far`.
        """
        max_so_far = float('-inf')
        current_max = 0

        for i in range(len(nums)):
            current_max += nums[i]

            if current_max > max_so_far:
                max_so_far = current_max

            if current_max < 0:
                current_max = 0

        return max_so_far
    return maxSubArray

# Test cases
def test_solution():
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    assert solution()(nums1) == 6

    nums2 = [1]
    assert solution()(nums2) == 1

    nums3 = [5,4,-1,7,8]
    assert solution()(nums3) == 23

    nums4 = [-1, -2, -3]
    assert solution()(nums4) == -1

    nums5 = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert solution()(nums5) == 7

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()