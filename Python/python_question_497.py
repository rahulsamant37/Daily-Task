# Python Question: Longest Increasing Subsequence with Given Starting Numbers
'''
Given an array of integers `nums` and a set of starting numbers `starts`, find the length of the longest increasing subsequence (LIS) of `nums` such that the subsequence must start with one of the numbers in `starts`.

An increasing subsequence is a subsequence of `nums` where the elements are in strictly increasing order.

Example:
Input: nums = [1, 3, 2, 4, 5], starts = {1, 2}
Output: 4
Explanation:
- If we start with 1, the LIS is [1, 2, 4, 5] or [1, 3, 4, 5], length is 4.
- If we start with 2, the LIS is [2, 4, 5], length is 3.
The maximum length is 4.

Input: nums = [10, 9, 2, 5, 3, 7, 101, 18], starts = {2, 3}
Output: 4
Explanation:
- If we start with 2, the LIS is [2, 5, 7, 101], length is 4.
- If we start with 3, the LIS is [3, 7, 101], length is 3.
The maximum length is 4.
'''

# Solution
def longest_increasing_subsequence_with_starts(nums, starts):
    """
    Finds the length of the longest increasing subsequence of nums that starts with one of the numbers in starts.

    Args:
        nums: A list of integers.
        starts: A set of integers that the subsequence must start with.

    Returns:
        The length of the longest increasing subsequence that starts with one of the numbers in starts.
    """

    def lis_from_start(start_val):
        """
        Helper function to calculate the LIS length starting from a specific value.
        """
        tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        for num in nums:
            if num >= start_val: # Consider only numbers greater or equal to start_val to ensure increasing order from start.
                if not tails or num > tails[-1]:
                    tails.append(num)
                else:
                    # Binary search to find the smallest tail that is greater than or equal to num.
                    l, r = 0, len(tails) - 1
                    while l <= r:
                        mid = (l + r) // 2
                        if tails[mid] < num:
                            l = mid + 1
                        else:
                            r = mid - 1
                    tails[l] = num
        return len(tails)
    
    max_len = 0
    for start in starts:
        max_len = max(max_len, lis_from_start(start))
    return max_len

# Test cases
def test_solution():
    nums1 = [1, 3, 2, 4, 5]
    starts1 = {1, 2}
    assert longest_increasing_subsequence_with_starts(nums1, starts1) == 4

    nums2 = [10, 9, 2, 5, 3, 7, 101, 18]
    starts2 = {2, 3}
    assert longest_increasing_subsequence_with_starts(nums2, starts2) == 4

    nums3 = [4, 10, 4, 3, 8, 9]
    starts3 = {4}
    assert longest_increasing_subsequence_with_starts(nums3, starts3) == 3

    nums4 = [5, 4, 3, 2, 1]
    starts4 = {1, 5}
    assert longest_increasing_subsequence_with_starts(nums4, starts4) == 1

    nums5 = [1, 2, 3, 4, 5]
    starts5 = {1}
    assert longest_increasing_subsequence_with_starts(nums5, starts5) == 5

    nums6 = [1, 2, 3, 4, 5]
    starts6 = {6}
    assert longest_increasing_subsequence_with_starts(nums6, starts6) == 0

    nums7 = [1, 2, 3, 4, 5]
    starts7 = {3, 4}
    assert longest_increasing_subsequence_with_starts(nums7, starts7) == 3

    nums8 = [2, 2, 2, 2, 2]
    starts8 = {2}
    assert longest_increasing_subsequence_with_starts(nums8, starts8) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()