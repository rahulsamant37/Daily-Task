# Python Question: Longest Increasing Subsequence with a Twist
'''
Given a list of integers `nums`, find the length of the longest increasing subsequence (LIS) with a twist. The twist is that you are only allowed to pick consecutive numbers from the input list to form the increasing subsequence.

For example:
Input: nums = [1, 3, 2, 4, 5]
Output: 3
Explanation: The longest increasing subsequence formed by consecutive elements is [2, 4, 5].

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 3
Explanation: The longest increasing subsequence formed by consecutive elements is [50, 60, 80].

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: The longest increasing subsequence formed by consecutive elements is [1, 2, 3, 4, 5].

Input: nums = [5, 4, 3, 2, 1]
Output: 1
Explanation: The longest increasing subsequence formed by consecutive elements is [5] or [4] or [3] or [2] or [1].
'''

# Solution
def longest_increasing_consecutive_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence (LIS) with a twist.
    The twist is that you are only allowed to pick consecutive numbers from the input list to form the increasing subsequence.

    Args:
      nums: A list of integers.

    Returns:
      The length of the longest increasing subsequence formed by consecutive elements.
    """

    if not nums:
        return 0

    n = len(nums)
    max_len = 1  # Initialize the maximum length to 1 (at least one element)

    # Iterate through all possible starting indices
    for i in range(n):
        current_len = 1  # Initialize the length of the current subsequence to 1
        last_num = nums[i]  # Initialize the last number in the subsequence

        # Iterate through the remaining elements in the list
        for j in range(i + 1, n):
            # If the current number is greater than the last number in the subsequence,
            # it can be added to the subsequence
            if nums[j] > last_num:
                current_len += 1  # Increment the length of the subsequence
                last_num = nums[j]  # Update the last number in the subsequence
            else:
                # If the current number is not greater than the last number,
                # the subsequence cannot be extended further from this point
                break

        # Update the maximum length if the current subsequence is longer
        max_len = max(max_len, current_len)

    return max_len


# Test cases
def test_solution():
    assert longest_increasing_consecutive_subsequence([1, 3, 2, 4, 5]) == 3
    assert longest_increasing_consecutive_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 3
    assert longest_increasing_consecutive_subsequence([1, 2, 3, 4, 5]) == 5
    assert longest_increasing_consecutive_subsequence([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_consecutive_subsequence([1]) == 1
    assert longest_increasing_consecutive_subsequence([]) == 0
    assert longest_increasing_consecutive_subsequence([1, 1, 1, 1, 1]) == 1
    assert longest_increasing_consecutive_subsequence([1, 2, 1, 2, 3]) == 3
    assert longest_increasing_consecutive_subsequence([3, 4, 2, 3, 4, 5]) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()