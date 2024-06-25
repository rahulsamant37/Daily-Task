# Python Question: Longest Consecutive Sequence
'''
Given an unsorted array of integers, find the length of the longest consecutive sequence (elements do not need to be adjacent in the original array).

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Therefore return its length 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore return its length 9.
'''

# Solution
def longest_consecutive(nums):
    """
    Finds the length of the longest consecutive sequence in an unsorted array of integers.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest consecutive sequence.
    """
    num_set = set(nums)  # Convert the list to a set for O(1) lookup
    longest_streak = 0

    for num in nums:
        # Check if the current number is the start of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            # Extend the sequence as long as the next number is in the set
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if the current streak is longer
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test cases
def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 2, 0, 1]) == 3
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([1, 2, 3, 4, 5]) == 5
    assert longest_consecutive([5, 4, 3, 2, 1]) == 5
    assert longest_consecutive([1, 3, 5, 7, 9]) == 1
    assert longest_consecutive([2, 6, 9, 1, 4, 0, 5, 3]) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_consecutive()