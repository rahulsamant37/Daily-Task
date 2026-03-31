# Python Question: Longest Increasing Subsequence with Modifications
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence. However, you are allowed to modify at most one element in the array to any other integer value to maximize the length of the longest increasing subsequence.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: Change 2 to 3. The longest increasing subsequence becomes [1, 3, 3, 4, 5] and its length is 5.

Input: nums = [1, 2, 3, 0, 5, 6]
Output: 6
Explanation: Change 0 to 4. The longest increasing subsequence becomes [1, 2, 3, 4, 5, 6] and its length is 6.

Input: nums = [5, 4, 3, 2, 1]
Output: 2
Explanation: Change 5 to 0 or 1 to 6. The longest increasing subsequence becomes [0, 4, 3, 2, 1] or [5, 4, 3, 2, 6] and its length is 2.

Input: nums = [1, 5, 2, 4, 3]
Output: 4
Explanation: Change 5 to 1. The longest increasing subsequence becomes [1, 1, 2, 4, 3] and its length is 4 ([1,2,4] after removing the second 1 or [1,2,3] after removing 4). Or change 3 to 5.
The longest increasing subsequence becomes [1, 5, 2, 4, 5] and its length is 4 ([1,2,4,5] after removing the first 5).
'''

# Solution
def longest_increasing_subsequence_with_modification(nums):
    """
    Finds the length of the longest increasing subsequence with at most one modification.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence with at most one modification.
    """

    n = len(nums)
    if n <= 1:
        return n

    def lis(arr):
        """
        Calculates the length of the longest increasing subsequence in an array.
        """
        tails = []
        for num in arr:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                l, r = 0, len(tails) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if tails[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                tails[l] = num
        return len(tails)

    max_len = lis(nums)  # Initial LIS without modification

    for i in range(n):
        original_val = nums[i]

        # Try modifying to smaller values
        nums[i] = float('-inf')  # Modify to a very small number
        max_len = max(max_len, lis(nums))

        # Try modifying to larger values
        nums[i] = float('inf')  # Modify to a very large number
        max_len = max(max_len, lis(nums))

        nums[i] = original_val  # Restore the original value

    return max_len

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 0, 5, 6]) == 6
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1]) == 2
    assert longest_increasing_subsequence_with_modification([1, 5, 2, 4, 3]) == 4
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([5, 5, 5, 5, 5]) == 2
    assert longest_increasing_subsequence_with_modification([1]) == 1
    assert longest_increasing_subsequence_with_modification([]) == 0
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 8
    assert longest_increasing_subsequence_with_modification([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()