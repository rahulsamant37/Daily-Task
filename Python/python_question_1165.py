# Python Question: Find the Missing Ranges
'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
Output: ["2", "4->49", "51->74", "76->99"]
'''

# Solution
def find_missing_ranges(nums, lower, upper):
    """
    Finds the missing ranges in a sorted integer array.

    Args:
        nums: A sorted integer array.
        lower: The lower bound of the inclusive range.
        upper: The upper bound of the inclusive range.

    Returns:
        A list of strings representing the missing ranges.
    """
    ranges = []
    nums = [lower - 1] + nums + [upper + 1]  # Add sentinels

    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]

        if diff == 2:
            ranges.append(str(nums[i - 1] + 1))
        elif diff > 2:
            ranges.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))

    return ranges

# Test cases
def test_solution():
    assert find_missing_ranges([0, 1, 3, 50, 75], 0, 99) == ["2", "4->49", "51->74", "76->99"]
    assert find_missing_ranges([], 1, 99) == ["1->99"]
    assert find_missing_ranges([0, 1, 2, 3, 7], 0, 7) == ["4->6"]
    assert find_missing_ranges([0, 1, 2, 3, 7], 0, 9) == ["4->6", "8->9"]
    assert find_missing_ranges([1, 2, 3, 4, 5], 0, 5) == ["0"]
    assert find_missing_ranges([1, 2, 3, 4, 5], 1, 5) == []
    assert find_missing_ranges([1, 2, 3, 4, 5], 0, 9) == ["0", "6->9"]
    assert find_missing_ranges([-1], -1, -1) == []
    assert find_missing_ranges([0], -1, 1) == ["-1", "1"]
    assert find_missing_ranges([0, 2, 4, 6], 0, 8) == ["1", "3", "5", "7->8"]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()