# Python Question: Find the Kth Largest Element in an Array After Removing Duplicates
'''
Given an array of integers `nums` and an integer `k`, find the kth largest element in the array *after* removing all duplicate elements.
For example, if `nums` is `[3, 2, 1, 5, 6, 4, 5]` and `k` is `2`, the unique elements are `[3, 2, 1, 5, 6, 4]` and the 2nd largest element is `5`.

Input:
nums = [3, 2, 1, 5, 6, 4, 5]
k = 2
Output:
5

Input:
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
Output:
3
'''

# Solution
def solution():
    def find_kth_largest_unique(nums, k):
        """
        Finds the kth largest element in the array after removing all duplicate elements.

        Args:
            nums: A list of integers.
            k: An integer representing the kth largest element to find.

        Returns:
            The kth largest element in the array after removing duplicates.
        """

        # Convert the list to a set to remove duplicate elements.
        unique_nums = sorted(list(set(nums)), reverse=True)

        # Check if k is within the valid range of the unique elements.
        if k > len(unique_nums) or k <= 0:
            return None  # Or raise an exception, depending on the desired behavior

        # Return the kth largest element. Note that lists are 0-indexed, so we subtract 1 from k.
        return unique_nums[k - 1]

    return find_kth_largest_unique
    # Test cases
def test_solution():
    find_kth_largest_unique = solution()

    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4, 5]
    k1 = 2
    expected1 = 5
    result1 = find_kth_largest_unique(nums1, k1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 3
    result2 = find_kth_largest_unique(nums2, k2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    expected3 = 5
    result3 = find_kth_largest_unique(nums3, k3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    k4 = 5
    expected4 = 1
    result4 = find_kth_largest_unique(nums4, k4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"

    # Test case 5
    nums5 = [1, 1, 1, 2, 2, 3]
    k5 = 2
    expected5 = 2
    result5 = find_kth_largest_unique(nums5, k5)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"

    # Test case 6: k is out of range
    nums6 = [1, 2, 3]
    k6 = 4
    expected6 = None
    result6 = find_kth_largest_unique(nums6, k6)
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()