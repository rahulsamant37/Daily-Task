# Python Question: Find the Largest Sum Contiguous Subarray with Circular Wrap

'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), find the maximum possible sum of a non-empty subarray.

A subarray may only include each element of the original array at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 != k2 such that nums[k1] == nums[k2].

Example:
Input: nums = [1,-2,3,-2]
Output: 4
Explanation: The subarray [3,-2,1] has the maximum possible sum of 4.

Input: nums = [5,-3,5]
Output: 10
Explanation: The subarray [5,5] has the maximum possible sum of 10.

Input: nums = [-3,-2,-3]
Output: -2
Explanation: The subarray [-2] has the maximum possible sum of -2.
'''

# Solution
def solution():
    def kadane(arr):
        # Kadane's Algorithm to find maximum sum contiguous subarray in a linear array
        max_so_far = float('-inf')
        current_max = 0
        for x in arr:
            current_max = max(x, current_max + x)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    def max_subarray_circular(nums):
        # 1. Find the maximum subarray sum using Kadane's algorithm for the linear array.
        max_kadane = kadane(nums)

        # 2. Find the maximum sum of the wrapped subarray.
        #    To do this, invert the sign of each element in the array and
        #    apply Kadane's algorithm to the inverted array.  The maximum
        #    sum of the inverted array represents the minimum sum of the original
        #    array. Subtract this minimum sum from the total sum to get the
        #    maximum sum of the wrapped subarray.
        arr_sum = 0
        for i in range(len(nums)):
            arr_sum += nums[i]
            nums[i] = -nums[i]

        max_wrap = arr_sum + kadane(nums)

        # 3. Return the maximum of the Kadane's result and the wrapped subarray result.
        # Special case: if all numbers are negative, max_wrap will be 0.
        # In that case, return the max_kadane, which will be the least negative number.
        if max_wrap > max_kadane and max_wrap != 0:
            return max_wrap
        else:
            return max_kadane

    return max_subarray_circular

# Test cases
def test_solution():
    nums1 = [1,-2,3,-2]
    assert solution()(nums1) == 4

    nums2 = [5,-3,5]
    assert solution()(nums2) == 10

    nums3 = [-3,-2,-3]
    assert solution()(nums3) == -2

    nums4 = [-2,-3,-1]
    assert solution()(nums4) == -1

    nums5 = [2,-2,2,7,-8,6,3]
    assert solution()(nums5) == 21

    nums6 = [2,1,-3,-4,5]
    assert solution()(nums6) == 6

    nums7 = [1]
    assert solution()(nums7) == 1

    nums8 = [-1]
    assert solution()(nums8) == -1

    nums9 = [1, -2, 3, -2]
    assert solution()(nums9) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()