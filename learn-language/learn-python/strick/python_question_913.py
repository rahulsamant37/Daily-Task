# Python Question: Longest Increasing Subsequence with Custom Comparison
'''
Given a list of tuples, where each tuple represents an item with two attributes: (weight, value). Find the length of the longest increasing subsequence (LIS) of these tuples, where the "increasing" condition is defined as follows:

A tuple (w1, v1) is considered smaller than (w2, v2) if and only if BOTH w1 < w2 and v1 < v2.  In other words, both the weight and value must be strictly increasing.

Example:
Input: [(1, 2), (2, 1), (3, 3), (4, 2), (5, 4)]
Output: 3
Explanation: The LIS is [(1, 2), (3, 3), (5, 4)].  (2, 1) is not smaller than (1, 2) because its value is smaller. (4, 2) is not smaller than (3, 3) because its value is smaller.

Input: [(1, 1), (2, 2), (3, 3)]
Output: 3

Input: [(3, 3), (2, 2), (1, 1)]
Output: 1

Input: [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
Output: 1

Input: []
Output: 0
'''

# Solution
def solution(items):
    """
    Finds the length of the longest increasing subsequence (LIS) of tuples.

    Args:
        items: A list of tuples, where each tuple is (weight, value).

    Returns:
        The length of the LIS.
    """

    if not items:
        return 0

    tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1.

    def is_smaller(item1, item2):
        """
        Checks if item1 is strictly smaller than item2 based on weight and value.
        """
        return item1[0] < item2[0] and item1[1] < item2[1]

    def binary_search(item):
        """
        Performs a binary search on the 'tails' list to find the smallest tail that is greater than or equal to the given item.
        """
        left, right = 0, len(tails) - 1
        while left <= right:
            mid = (left + right) // 2
            if is_smaller(tails[mid], item):  # tails[mid] < item
                left = mid + 1
            else:
                right = mid - 1
        return left  # Returns the index where the item should be inserted

    for item in items:
        i = binary_search(item)
        if i == len(tails):
            tails.append(item)  # Extends the longest increasing subsequence
        else:
            tails[i] = item  # Replace the smallest tail with a smaller one

    return len(tails)  # The length of tails is the length of the LIS

# Test cases
def test_solution():
    assert solution([(1, 2), (2, 1), (3, 3), (4, 2), (5, 4)]) == 3
    assert solution([(1, 1), (2, 2), (3, 3)]) == 3
    assert solution([(3, 3), (2, 2), (1, 1)]) == 1
    assert solution([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]) == 1
    assert solution([]) == 0
    assert solution([(1,2)]) == 1
    assert solution([(5,4), (1,2)]) == 1
    assert solution([(1, 2), (3, 4), (2, 3)]) == 2
    assert solution([(1, 2), (2, 3), (3, 4)]) == 3
    assert solution([(1,2), (4,5), (2,3), (3,4)]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()