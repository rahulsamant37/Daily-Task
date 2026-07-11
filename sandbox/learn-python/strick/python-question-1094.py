# Python Question: Longest Increasing Subsequence with Modification
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence.
However, you are allowed to modify at most one element of the array to any other integer value. Find the maximum possible length of the longest increasing subsequence after this modification.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: Modify 2 to 3. The array becomes [1, 3, 3, 4, 5]. The LIS is [1, 3, 4, 5] with length 4. However, if modify 3 to 2. The array becomes [1, 2, 2, 4, 5]. The LIS is [1, 2, 4, 5] with length 4.
If we modify 2 to any number between 1 and 3. The array becomes [1, 3, x, 4, 5]. The LIS is [1, 3, 4, 5] with length 4.
If we modify 3 to any number between 1 and 2. The array becomes [1, x, 2, 4, 5]. The LIS is [1, 2, 4, 5] with length 4.
If we modify 3 to 4. The array becomes [1, 4, 2, 4, 5]. The LIS is [1, 2, 4, 5] with length 4.
If we modify 2 to 1. The array becomes [1, 3, 1, 4, 5]. The LIS is [1, 3, 4, 5] with length 4.
If we modify 2 to 6. The array becomes [1, 3, 6, 4, 5]. The LIS is [1, 3, 4, 5] with length 4.
If we modify nums[2] (2) to 3, the array becomes [1, 3, 3, 4, 5], and the LIS is [1, 3, 4, 5] with length 4.
However, if we modify nums[2] (2) to a value greater than 3, say 6, the array becomes [1, 3, 6, 4, 5]. The LIS is [1, 3, 4, 5] with length 4.
If we modify nums[0] (1) to a value greater than 5, say 6, the array becomes [6, 3, 2, 4, 5]. The LIS is [3, 4, 5] with length 3.
If we modify nums[1] (3) to 0, the array becomes [1, 0, 2, 4, 5]. The LIS is [1, 2, 4, 5] with length 4.
If we modify nums[2] (2) to 0, the array becomes [1, 3, 0, 4, 5]. The LIS is [1, 3, 4, 5] with length 4.
If we modify nums[3] (4) to 0, the array becomes [1, 3, 2, 0, 5]. The LIS is [1, 3, 5] with length 3.
If we modify nums[4] (5) to 0, the array becomes [1, 3, 2, 4, 0]. The LIS is [1, 3, 4] with length 3.
If we modify 3 to 2, array becomes [1, 2, 2, 4, 5]. LIS is [1, 2, 4, 5], length is 4.
If we don't modify any element, the LIS is [1, 2, 4, 5] with length 4. If we modify 3 to 1, array is [1, 1, 2, 4, 5], LIS is [1, 2, 4, 5].

Input: nums = [5, 4, 3, 2, 1]
Output: 2
Explanation: Modify 5 to 0. The array becomes [0, 4, 3, 2, 1]. The LIS is [0, 1] with length 2.

Input: nums = [1, 2, 3, 4, 5]
Output: 5

Input: nums = [1, 3, 2, 4, 5]
Output: 5

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 8

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input: nums = [2,2,2,2,2]
Output: 2
'''

# Solution
def longest_increasing_subsequence_with_modification(nums):
    """
    Finds the length of the longest strictly increasing subsequence after modifying at most one element.

    Args:
        nums: A list of integers.

    Returns:
        The maximum possible length of the longest increasing subsequence.
    """

    n = len(nums)
    if n <= 1:
        return n

    def calculate_lis_length(arr):
        """Calculates the length of the longest increasing subsequence."""
        tails = []
        for num in arr:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                # Binary search to find the smallest element in tails that is greater than or equal to num
                l, r = 0, len(tails) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if tails[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                tails[l] = num  # Replace the smallest element >= num with num
        return len(tails)

    max_lis_length = calculate_lis_length(nums)  # LIS without modification

    for i in range(n):
        original_value = nums[i]

        # Try modifying to a smaller value (smaller than all values before it)
        temp_nums1 = nums[:]
        if i > 0:
            temp_nums1[i] = nums[0] - 1
        else:
            temp_nums1[i] = -1  # If first element, modify to -1

        max_lis_length = max(max_lis_length, calculate_lis_length(temp_nums1))

        # Try modifying to a larger value (larger than all values after it)
        temp_nums2 = nums[:]
        if i < n - 1:
            temp_nums2[i] = nums[-1] + 1
        else:
            temp_nums2[i] = 10**9 + 1  # If last element, modify to a large value

        max_lis_length = max(max_lis_length, calculate_lis_length(temp_nums2))

        nums[i] = original_value  # Restore original value

    return max_lis_length

# Test cases
def test_solution():
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([5, 4, 3, 2, 1]) == 2
    assert longest_increasing_subsequence_with_modification([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_subsequence_with_modification([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 8
    assert longest_increasing_subsequence_with_modification([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence_with_modification([2,2,2,2,2]) == 2
    assert longest_increasing_subsequence_with_modification([1, 100]) == 2
    assert longest_increasing_subsequence_with_modification([100, 1]) == 2
    assert longest_increasing_subsequence_with_modification([1, 5, 2, 3, 4]) == 5
    assert longest_increasing_subsequence_with_modification([5, 1, 5, 2, 6, 3, 4]) == 5
    assert longest_increasing_subsequence_with_modification([1, 3, 2, 4, 1, 5]) == 5
    assert longest_increasing_subsequence_with_modification([1, 3, 5, 2, 4, 6]) == 6
    assert longest_increasing_subsequence_with_modification([1, 1, 1]) == 2
    assert longest_increasing_subsequence_with_modification([1]) == 1
    assert longest_increasing_subsequence_with_modification([]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()