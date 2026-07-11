# Python Question: Longest Consecutive Sequence
'''
Given an unsorted array of integers, find the length of the longest consecutive sequence
(elements need not be adjacent in the original array).

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# Solution
def longestConsecutive(nums):
    """
    Finds the length of the longest consecutive sequence in an unsorted array of integers.

    Args:
      nums: A list of integers.

    Returns:
      The length of the longest consecutive sequence.
    """
    if not nums:
        return 0

    num_set = set(nums)  # Convert the list to a set for efficient lookup (O(1) on average)
    longest_sequence = 0

    for num in nums:
        # Check if the current number is the start of a sequence
        # We determine if it's the start by checking if num-1 is not in the set.
        if (num - 1) not in num_set:
            current_num = num
            current_sequence_length = 1

            # Extend the sequence as much as possible
            while (current_num + 1) in num_set:
                current_num += 1
                current_sequence_length += 1

            # Update the longest sequence if necessary
            longest_sequence = max(longest_sequence, current_sequence_length)

    return longest_sequence

# Test cases
def test_longestConsecutive():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longestConsecutive([1, 2, 0, 1]) == 3
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1, 2, 3, 4, 5]) == 5
    assert longestConsecutive([5, 4, 3, 2, 1]) == 5
    assert longestConsecutive([1, 3, 5, 7, 9]) == 1
    assert longestConsecutive([1, 2, 2, 3, 4]) == 4
    assert longestConsecutive([9,1,4,7,3,-1,0,5,-3]) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_longestConsecutive()