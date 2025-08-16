# Python Question: Find the Kth Largest Element in an Array
'''
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

You must solve it in O(n) average time complexity.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# Solution
import random

def findKthLargest(nums, k):
    """
    Finds the kth largest element in an array using the QuickSelect algorithm.

    Args:
        nums: The input array of integers.
        k: The desired kth largest element.

    Returns:
        The kth largest element in the array.
    """
    def partition(l, r):
        """
        Partitions the subarray nums[l:r+1] around a pivot element.

        The pivot is chosen randomly. Elements smaller than the pivot are moved to the left,
        and elements larger than the pivot are moved to the right.

        Args:
            l: The left index of the subarray.
            r: The right index of the subarray.

        Returns:
            The index of the pivot element after partitioning.
        """
        pivot_index = random.randint(l, r)
        nums[r], nums[pivot_index] = nums[pivot_index], nums[r]  # Move pivot to the end
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]  # Move pivot to its correct position
        return i

    def quickselect(l, r, k):
        """
        Recursively selects the kth largest element using the QuickSelect algorithm.

        Args:
            l: The left index of the subarray.
            r: The right index of the subarray.
            k: The desired kth largest element (relative to the subarray).

        Returns:
            The kth largest element in the subarray.
        """
        if l == r:
            return nums[l]

        pivot_index = partition(l, r)
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quickselect(l, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, r, k)

    # kth largest is equivalent to (n - k)th smallest (0-indexed)
    return quickselect(0, len(nums) - 1, len(nums) - k)

# Test cases
def test_solution():
    """
    Tests the findKthLargest function with various test cases.
    """
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7, 6, 5, 4, 3, 2, 1], 3, 5),
        ([1], 1, 1),
        ([1, 2], 1, 2),
        ([1, 2], 2, 1),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),
        ([5, 2, 4, 1, 3, 6, 0], 4, 3),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 5, 4)
    ]

    for nums, k, expected in test_cases:
        actual = findKthLargest(nums.copy(), k)  # Use a copy to avoid modifying the original list
        assert actual == expected, f"Input: nums={nums}, k={k}, Expected: {expected}, Actual: {actual}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()