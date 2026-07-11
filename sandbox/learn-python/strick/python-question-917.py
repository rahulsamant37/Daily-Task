# Python Question: Longest Consecutive Sequence
'''
Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore return its length 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# Solution
def longestConsecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence in O(n) time.

    Args:
        nums: An unsorted array of integers.

    Returns:
        The length of the longest consecutive elements sequence.
    """
    # Convert the list to a set for O(1) lookups.
    num_set = set(nums)
    longest_streak = 0

    # Iterate through the numbers in the set.
    for num in num_set:
        # Check if the current number is the start of a sequence.
        # A number is the start of a sequence if num - 1 is not in the set.
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1

            # While the next number in the sequence is in the set, increment the streak.
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if the current streak is longer.
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test cases
def test_longestConsecutive():
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longestConsecutive([1,2,0,1]) == 3
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1,2,3,4,5]) == 5
    assert longestConsecutive([5,4,3,2,1]) == 5
    assert longestConsecutive([1]) == 1
    assert longestConsecutive([1,1,1,1,1]) == 1
    assert longestConsecutive([9,1,4,7,3,-1,0,5,-3]) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_longestConsecutive()