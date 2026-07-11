# Python Question: Largest Sum Contiguous Subarray with Modification

'''
Given an array of integers `nums`, find the contiguous subarray (containing at least one number) which has the largest sum. However, you are allowed to change at most one element in the array to any other integer. Your task is to find the maximum possible sum of a contiguous subarray after making at most one modification.

Example:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6. We don't need to modify any element.

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, -10, 6]
Output: 7
Explanation: We can modify -10 to 1, resulting in the subarray [4, -1, 2, 1, -5, 4, 1, 6] with a sum of 12. But we can achieve a maximum subarray sum of 7 by modifying -5 to 1, resulting in the subarray [4, -1, 2, 1, 1] with sum 7. We can also modify -3 to 4 to get [4, -1, 4, 4, -1, 2, 1] with a sum of 13. It turns out that changing -10 to some large number will not change the maximum contiguous subarray sum.
Input: nums = [-1,-1,-1,-1]
Output: 0
Explanation: Change any element to a large number like 100, then the maximum sum will be 100. Kadane algorithm will return -1. In this case, we could change one -1 to 0, then Kadane algorithm will return 0.

'''

# Solution
def solution():
    def max_subarray_sum(nums):
        """
        Kadane's algorithm to find the maximum sum contiguous subarray.
        """
        max_so_far = float('-inf')
        current_max = 0
        for num in nums:
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    def solve(nums):
        n = len(nums)
        max_sum = max_subarray_sum(nums)  # Maximum sum without modification

        for i in range(n):
            original_value = nums[i]
            
            # Optimization: Try changing nums[i] to the maximum value in the array,
            # or set it to 0 if all the numbers are negative or zero.
            max_val = max(nums) if any(x > 0 for x in nums) else 0
            nums[i] = max_val

            max_sum = max(max_sum, max_subarray_sum(nums))
            nums[i] = original_value  # Restore the original value

        return max_sum

    return solve
    

# Test cases
def test_solution():
    solve = solution()
    
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    assert solve(nums1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {solve(nums1)}"

    # Test case 2
    nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, -10, 6]
    expected2 = 7
    assert solve(nums2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {solve(nums2)}"

    # Test case 3
    nums3 = [-1, -1, -1, -1]
    expected3 = 0
    assert solve(nums3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {solve(nums3)}"

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    expected4 = 15
    assert solve(nums4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {solve(nums4)}"
    
    # Test case 5
    nums5 = [-10]
    expected5 = 0
    assert solve(nums5) == 0, f"Test Case 5 Failed: Expected {0}, Got {solve(nums5)}"

    # Test case 6
    nums6 = [-1, -2, -3]
    expected6 = 0
    assert solve(nums6) == 0, f"Test Case 6 Failed: Expected {0}, Got {solve(nums6)}"
    
    # Test case 7
    nums7 = [0,0,0]
    expected7 = 0
    assert solve(nums7) == 0, f"Test Case 7 Failed: Expected {expected7}, Got {solve(nums7)}"
    
    # Test case 8
    nums8 = [-5, -2, 4, -1, -2, 1, 5, -3]
    expected8 = 12
    assert solve(nums8) == 12, f"Test Case 8 Failed: Expected {expected8}, Got {solve(nums8)}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()