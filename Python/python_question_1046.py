# Python Question: Longest Increasing Subsequence with Limited Range
'''
Given an array of integers `nums` where each element is within the range [1, k] (inclusive),
find the length of the longest strictly increasing subsequence (LIS) of `nums`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 5
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 4, 5].

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], k = 80
Output: 6
Explanation: The longest increasing subsequence is [10, 22, 33, 50, 60, 80].

Input: nums = [1, 5, 2, 4, 3], k = 5
Output: 3
Explanation: The longest increasing subsequence is [1, 2, 3] or [1, 2, 4] or [1, 3, 4] or [1, 3, 5].
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums, k):
        """
        Finds the length of the longest strictly increasing subsequence (LIS) of `nums`.
        This implementation uses dynamic programming with binary search optimization
        to achieve a time complexity of O(n log k), where n is the length of nums
        and k is the upper bound of the elements in nums.

        Args:
          nums: A list of integers.
          k: The upper bound of the elements in nums.

        Returns:
          The length of the LIS.
        """

        tails = []  # Stores the smallest tail of all increasing subsequences with length i+1 in tails[i].

        for num in nums:
            # If we find a number in tails that is greater than or equal to num,
            # it means we can replace that number with num to get a smaller tail
            # for an increasing subsequence of the same length.

            # Binary search to find the smallest tail that is >= num
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any such number (l == len(tails)), it means we can extend
            # the longest increasing subsequence by 1 by appending num to it.
            if l == len(tails):
                tails.append(num)
            else:
                # Otherwise, we replace the smallest tail that is >= num with num.
                tails[l] = num

        return len(tails)

    return longest_increasing_subsequence
    

# Test cases
def test_solution():
    lis_func = solution()

    # Test case 1
    nums1 = [1, 3, 2, 4, 5]
    k1 = 5
    expected1 = 4
    assert lis_func(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {lis_func(nums1, k1)}"

    # Test case 2
    nums2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k2 = 80
    expected2 = 6
    assert lis_func(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {lis_func(nums2, k2)}"

    # Test case 3
    nums3 = [1, 5, 2, 4, 3]
    k3 = 5
    expected3 = 3
    assert lis_func(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {lis_func(nums3, k3)}"

    # Test case 4: Empty array
    nums4 = []
    k4 = 10
    expected4 = 0
    assert lis_func(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {lis_func(nums4, k4)}"

    # Test case 5: All same elements
    nums5 = [5, 5, 5, 5, 5]
    k5 = 5
    expected5 = 1
    assert lis_func(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {lis_func(nums5, k5)}"

    # Test case 6: Decreasing order
    nums6 = [5, 4, 3, 2, 1]
    k6 = 5
    expected6 = 1
    assert lis_func(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {lis_func(nums6, k6)}"

    # Test case 7: Single element
    nums7 = [7]
    k7 = 7
    expected7 = 1
    assert lis_func(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {lis_func(nums7, k7)}"

    # Test case 8: k=1, all elements are 1
    nums8 = [1,1,1,1]
    k8 = 1
    expected8 = 1
    assert lis_func(nums8, k8) == expected8, f"Test Case 8 Failed: Expected {expected8}, got {lis_func(nums8, k8)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()