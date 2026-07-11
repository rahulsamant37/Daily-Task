# Python Question: Longest Increasing Subsequence with Minimum Ending Value
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS).
If there are multiple LIS with the same length, return the LIS that has the minimum ending value.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: The longest increasing subsequence is [1, 2, 4, 5], which has a length of 4 and ends with 5.
Another LIS is [1, 3, 4, 5], which also has a length of 4 and ends with 5.
The LIS [1, 2, 4, 5] should be returned (implicitly by returning its length 4).

Input: nums = [1, 5, 2, 4, 3]
Output: 4
Explanation: The longest increasing subsequence is [1, 2, 4], which has a length of 3 and ends with 4.
Another LIS is [1, 2, 3], which also has a length of 3 and ends with 3.
The LIS [1, 2, 3] should be implicitly preferred as it ends with a smaller value.

Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 18], which has a length of 4 and ends with 18.
Another LIS is [2, 5, 7, 18], which also has a length of 4 and ends with 18.
The LIS [2, 3, 7, 18] should be implicitly preferred as it ends with a smaller value than other LIS of same length.
'''

# Solution
def longest_increasing_subsequence_with_minimum_ending_value(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) in the given array.
    If there are multiple LIS with the same length, it returns the length of the LIS that has the minimum ending value.

    Args:
        nums: A list of integers.

    Returns:
        The length of the LIS with the minimum ending value.
    """

    # tails[i] is the smallest tail of all increasing subsequences with length i+1.
    tails = []

    for num in nums:
        if not tails or num > tails[-1]:
            # If num is greater than the current largest tail, extend the longest subsequence.
            tails.append(num)
        else:
            # Otherwise, find the smallest tail that is greater than or equal to num
            # and replace it with num. This maintains the property that tails[i] is the
            # smallest tail of all increasing subsequences with length i+1.
            # We use binary search to find the smallest tail that is greater than or equal to num.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            tails[l] = num

    return len(tails)


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_minimum_ending_value([1, 3, 2, 4, 5]) == 4
    assert longest_increasing_subsequence_with_minimum_ending_value([1, 5, 2, 4, 3]) == 3
    assert longest_increasing_subsequence_with_minimum_ending_value([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence_with_minimum_ending_value([0,1,0,3,2,3]) == 4
    assert longest_increasing_subsequence_with_minimum_ending_value([7,7,7,7,7,7,7]) == 1
    assert longest_increasing_subsequence_with_minimum_ending_value([]) == 0
    assert longest_increasing_subsequence_with_minimum_ending_value([1]) == 1
    assert longest_increasing_subsequence_with_minimum_ending_value([2,2]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()