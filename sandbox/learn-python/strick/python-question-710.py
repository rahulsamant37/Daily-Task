# Python Question: Longest Increasing Subsequence with Minimum Last Element
'''
Given a list of integers, find the longest increasing subsequence (LIS). If multiple LISs exist with the same length, return the one with the minimum last element.

Example:
Input: [1, 3, 2, 4, 5]
Output: [1, 2, 4, 5]

Input: [5, 2, 8, 6, 3, 6, 9, 5]
Output: [2, 3, 6, 9]
'''

# Solution
def longest_increasing_subsequence_min_last(nums):
    """
    Finds the longest increasing subsequence (LIS) with the minimum last element.

    Args:
        nums: A list of integers.

    Returns:
        A list representing the LIS with the minimum last element.
    """

    if not nums:
        return []

    tails = []  # tails[i] is the smallest tail of all increasing subsequences with length i+1
    predecessors = {}  # predecessors[x] is the predecessor of x in the LIS ending with x

    for num in nums:
        # If we find a number in `tails` that is greater or equal to the current number,
        # it means we can potentially extend an existing subsequence with the current number
        # while keeping the tail smaller than before.
        if tails and num <= tails[-1]:
            # Binary search to find the smallest tail >= num
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # Replace the found tail with the current number.
            # This doesn't change the length of the LIS, but it potentially makes
            # the tail smaller, which is what we want.
            if l > 0:
                predecessors[num] = tails[l - 1]
            tails[l] = num
        else:
            # If the current number is greater than all tails, it extends the LIS by 1.
            if tails:
                predecessors[num] = tails[-1]
            tails.append(num)

    # Reconstruct the LIS from the `tails` and `predecessors` dictionaries.
    # Start from the last element of the longest subsequence (which is the last element in `tails`).
    longest_subsequence = []
    current = tails[-1]
    while current is not None:
        longest_subsequence.append(current)
        current = predecessors.get(current)

    return longest_subsequence[::-1]  # Reverse the list to get the correct order

# Test cases
def test_solution():
    assert longest_increasing_subsequence_min_last([1, 3, 2, 4, 5]) == [1, 2, 4, 5]
    assert longest_increasing_subsequence_min_last([5, 2, 8, 6, 3, 6, 9, 5]) == [2, 3, 6, 9]
    assert longest_increasing_subsequence_min_last([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 41, 60, 80]
    assert longest_increasing_subsequence_min_last([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence_min_last([5, 4, 3, 2, 1]) == [5]
    assert longest_increasing_subsequence_min_last([1, 3, 2, 4, 1, 5]) == [1, 2, 4, 5]
    assert longest_increasing_subsequence_min_last([]) == []
    assert longest_increasing_subsequence_min_last([1]) == [1]
    assert longest_increasing_subsequence_min_last([1, 1, 1, 1]) == [1]
    assert longest_increasing_subsequence_min_last([4, 2, 4, 5, 3, 7]) == [2, 4, 5, 7]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()