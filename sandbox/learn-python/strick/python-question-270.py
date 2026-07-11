# Python Question: Longest Consecutive Sequence
'''
Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# Solution
def longestConsecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence in an unsorted array of integers.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest consecutive elements sequence.
    """
    num_set = set(nums)  # Convert the list to a set for O(1) lookup time
    longest_streak = 0

    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Extend the sequence as far as possible
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test cases
def test_longestConsecutive():
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longestConsecutive([1,2,0,1]) == 3
    assert longestConsecutive([9,1,4,7,3,-1,0,5,-1,6]) == 7
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1]) == 1
    assert longestConsecutive([1,2]) == 2
    assert longestConsecutive([2,1]) == 2
    assert longestConsecutive([1,2,3,4,5]) == 5
    assert longestConsecutive([5,4,3,2,1]) == 5
    assert longestConsecutive([1, 3, 5, 2, 4]) == 5

if __name__ == "__main__":
    test_longestConsecutive()