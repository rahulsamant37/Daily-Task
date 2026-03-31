# Python Question: Longest Increasing Subsequence with Given Start
'''
Given an array of integers `nums` and a starting index `start`, find the length of the longest increasing subsequence (LIS) that starts at `nums[start]`.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 3, 2, 4, 5], start = 0
Output: 4
Explanation: The longest increasing subsequence starting at nums[0] (which is 1) is [1, 2, 4, 5].

Input: nums = [5, 4, 3, 2, 1], start = 0
Output: 1
Explanation: The longest increasing subsequence starting at nums[0] (which is 5) is [5].

Input: nums = [10, 22, 9, 33, 21, 50, 41, 60, 80], start = 0
Output: 6
Explanation: The longest increasing subsequence starting at nums[0] (which is 10) is [10, 22, 33, 50, 60, 80].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_start(nums, start):
        """
        Finds the length of the longest increasing subsequence (LIS) in `nums` that starts at `nums[start]`.

        Args:
            nums: A list of integers.
            start: The starting index.

        Returns:
            The length of the LIS.
        """

        n = len(nums)
        if start >= n:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at index i
        # starting from nums[start].
        dp = {}  # Use a dictionary for memoization (index, last_element): length

        def lis_recursive(index, last_element):
            """
            Recursive helper function to calculate the LIS length.

            Args:
                index: The current index being considered.
                last_element: The value of the last element included in the subsequence.

            Returns:
                The length of the LIS starting from nums[start] and ending at index `index`.
            """
            if index == n:
                return 0

            if (index, last_element) in dp:
                return dp[(index, last_element)]

            # Option 1: Exclude the current element.
            exclude = lis_recursive(index + 1, last_element)

            # Option 2: Include the current element if it's greater than the last element.
            include = 0
            if nums[index] > last_element:
                include = 1 + lis_recursive(index + 1, nums[index])

            dp[(index, last_element)] = max(include, exclude)
            return dp[(index, last_element)]

        return lis_recursive(start, float('-inf'))
    
    return longest_increasing_subsequence_with_start

# Test cases
def test_solution():
    nums1 = [1, 3, 2, 4, 5]
    start1 = 0
    expected1 = 4
    assert solution()(nums1, start1) == expected1

    nums2 = [5, 4, 3, 2, 1]
    start2 = 0
    expected2 = 1
    assert solution()(nums2, start2) == expected2

    nums3 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    start3 = 0
    expected3 = 6
    assert solution()(nums3, start3) == expected3

    nums4 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    start4 = 2
    expected4 = 5
    assert solution()(nums4, start4) == 5

    nums5 = [2, 2, 2, 2, 2]
    start5 = 0
    expected5 = 1
    assert solution()(nums5, start5) == 1

    nums6 = [1, 2, 3, 4, 5]
    start6 = 4
    expected6 = 1
    assert solution()(nums6, start6) == 1

    nums7 = [1, 2, 3, 4, 5]
    start7 = 0
    expected7 = 5
    assert solution()(nums7, start7) == 5

    nums8 = [1]
    start8 = 0
    expected8 = 1
    assert solution()(nums8, start8) == 1

    nums9 = []
    start9 = 0
    expected9 = 0
    try:
        solution()([], 0)
    except IndexError:
        pass
    else:
        assert False, "IndexError was not raised for empty list"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()