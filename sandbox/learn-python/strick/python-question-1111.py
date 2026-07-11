# Python Question: Find the Longest Consecutive Sequence
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

# Solution
def longest_consecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence in an unsorted array of integers.

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

            # While the next number is in the set, increment the streak and move to the next number
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
    assert longest_consecutive([1, 3, 5, 2, 4]) == 5
    assert longest_consecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,-9,1,9,-4,-4,5,-7,-1,0,8,-6]) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_consecutive()