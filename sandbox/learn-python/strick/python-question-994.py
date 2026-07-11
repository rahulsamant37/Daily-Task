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
        nums: A list of integers.
        k: The kth largest element to find (1-indexed).

    Returns:
        The kth largest element in the array.
    """
    def partition(left, right, pivot_index):
        """
        Partitions the array around the pivot.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            pivot_index: The index of the pivot element.

        Returns:
            The index of the pivot after partitioning.
        """
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def quickselect(left, right, k_smallest):
        """
        Performs the QuickSelect algorithm to find the kth smallest element.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            k_smallest: The kth smallest element to find (0-indexed).

        Returns:
            The kth smallest element in the subarray.
        """
        if left == right:
            return nums[left]

        # select a random pivot_index
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)


# Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            print(f"Assertion failed: {message}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
            raise AssertionError

    nums1 = [3,2,1,5,6,4]
    k1 = 2
    assert_equal(findKthLargest(nums1, k1), 5, "Test Case 1 Failed")

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    assert_equal(findKthLargest(nums2, k2), 4, "Test Case 2 Failed")

    nums3 = [1]
    k3 = 1
    assert_equal(findKthLargest(nums3, k3), 1, "Test Case 3 Failed")

    nums4 = [2,1]
    k4 = 1
    assert_equal(findKthLargest(nums4, k4), 2, "Test Case 4 Failed")

    nums5 = [2,1]
    k5 = 2
    assert_equal(findKthLargest(nums5, k5), 1, "Test Case 5 Failed")

    nums6 = [7,6,5,4,3,2,1]
    k6 = 5
    assert_equal(findKthLargest(nums6, k6), 3, "Test Case 6 Failed")

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()