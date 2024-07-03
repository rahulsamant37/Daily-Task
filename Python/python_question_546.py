# Python Question: Longest Increasing Subsequence with Modifications
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence. However, you are allowed to modify the array *at most once* by changing a single element to any other integer value. The modification can be any value, it doesn't have to be within the range of the original array.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: We can change 2 to any number less than 3 (e.g., 1) to make the sequence strictly increasing.

Input: nums = [1, 3, 5, 0, 7]
Output: 5
Explanation: We can change 0 to any number greater than 5 (e.g., 6) to make the sequence strictly increasing.

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: The array is already strictly increasing, so no modification is needed.

Input: nums = [5, 4, 3, 2, 1]
Output: 2
Explanation: We can change any element to make the sequence increasing. For example, we can change 5 to 0, resulting in [0, 4, 3, 2, 1]. The LIS is [0,4]. We can change 4 to 6, resulting in [5, 6, 3, 2, 1], the LIS is [5,6]. We can change 3 to 7, resulting in [5, 4, 7, 2, 1], the LIS is [5, 7]. We can change 2 to 8, resulting in [5, 4, 3, 8, 1], the LIS is [5, 8]. We can change 1 to 9, resulting in [5, 4, 3, 2, 9], the LIS is [5,9]. Changing 3 to -1 results in [5, 4, -1, 2, 1], the LIS is [5]. Changing 4 to 0 gives [5, 0, 3, 2, 1], the LIS is [5].

'''

# Solution
def longest_increasing_subsequence_with_modification(nums):
    """
    Calculates the length of the longest increasing subsequence with at most one modification allowed.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest increasing subsequence with at most one modification.
    """

    n = len(nums)
    if n <= 1:
        return n

    def calculate_lis(arr):
        """
        Calculates the length of the longest increasing subsequence using dynamic programming.
        """
        tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        for num in arr:
            if not tails or num > tails[-1]:
                tails.append(num)  # Extend the longest increasing subsequence found so far.
            else:
                # Find the smallest tail that is greater than or equal to the current number using binary search
                l, r = 0, len(tails) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if tails[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                tails[l] = num  # Replace the tail with the current number to potentially form a longer subsequence later.
        return len(tails)

    max_lis = calculate_lis(nums)  # LIS without any modification

    for i in range(n):
        original_value = nums[i]

        # Try modifying to a small value
        nums[i] = float('-inf') # Very small value
        max_lis = max(max_lis, calculate_lis(nums))

        # Try modifying to a large value
        nums[i] = float('inf') # Very large value
        max_lis = max(max_lis, calculate_lis(nums))

        # Restore the original value
        nums[i] = original_value
    return max_lis


# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([1, 3, 5, 0, 7]) == 5
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1]) == 2
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 8
    assert longest_increasing_subsequence_with_modification([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
    assert longest_increasing_subsequence_with_modification([1]) == 1
    assert longest_increasing_subsequence_with_modification([]) == 0
    assert longest_increasing_subsequence_with_modification([2,2,2,2,2]) == 2
    assert longest_increasing_subsequence_with_modification([1,5,2,4,3]) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()