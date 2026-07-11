# Python Question: Find the Longest Increasing Subsequence with a Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) in `nums` that sums up to the `target`.  If no such subsequence exists, return 0.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a subsequence where the elements are in strictly increasing order.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: 4
Explanation: The longest increasing subsequence that sums to 9 is [1, 2, 3, 4], which has a length of 4.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: There is no increasing subsequence that sums to 10.

Input: nums = [1, 5, 2, 9, 3, 7, 4], target = 15
Output: 3
Explanation: One possible LIS summing to 15 is [1, 7, 7] which is not increasing. Another one is [1, 5, 9] which is not increasing.  [1, 5, 9] sums to 15, but it is not increasing. Another one is [1, 2, 3, 4, 5] that sums to 15. [1, 2, 3, 9] sums to 15.
[1, 5, 9] has length 3.
[1, 2, 3, 4, 5] sums to 15, but it's not increasing.
[1, 2, 3, 4, 5] = 15. The length is 5, but it is not increasing.
[1, 2, 3, 4, 5] sums to 15, but the problem requires the subsequence to be increasing.
[1, 5, 2, 9, 3, 7, 4], target = 15
[1, 5, 9] -> increasing, sum = 15, length = 3
[1, 2, 3, 4, 5] does not work since not increasing.
[1, 2, 3, 7] is increasing, sum = 13.
[1, 2, 4, 7] is increasing, sum = 14.
[1, 2, 3, 9] is not increasing
[1, 2, 3, 7] sum is 13
[2, 3, 4, 6]
'''

# Solution
def solution():
    def longest_increasing_subsequence_sum(nums, target):
        """
        Finds the length of the longest increasing subsequence (LIS) in nums that sums up to the target.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            The length of the longest increasing subsequence that sums up to the target, or 0 if no such subsequence exists.
        """
        n = len(nums)
        dp = {}  # memoization: (index, current_sum, last_element) -> length of LIS

        def solve(index, current_sum, last_element):
            """
            Recursive helper function to find the LIS length.

            Args:
                index: The current index in nums.
                current_sum: The current sum of the subsequence.
                last_element: The last element added to the subsequence (used to maintain increasing order).

            Returns:
                The length of the LIS ending at index that sums up to the target.
            """
            if current_sum == target:
                return 0  # Base case: target sum reached, return 0 to indicate no more elements needed. Could be the start of a new increasing sequence
            if index == n:
                return float('-inf')  # Base case: end of array, return -inf if target not reached. We want to filter out invalid sequences.

            if (index, current_sum, last_element) in dp:
                return dp[(index, current_sum, last_element)]

            # Option 1: Exclude the current element
            exclude = solve(index + 1, current_sum, last_element)

            # Option 2: Include the current element if it's greater than the last element and doesn't exceed the target sum
            include = float('-inf')
            if nums[index] > last_element and current_sum + nums[index] <= target:
                include = 1 + solve(index + 1, current_sum + nums[index], nums[index])

            dp[(index, current_sum, last_element)] = max(exclude, include)
            return dp[(index, current_sum, last_element)]

        result = solve(0, 0, float('-inf'))  # Start with index 0, sum 0, and a very small last element to allow any number to be included first.
        return max(0, result)  # If no LIS is found, return 0.

    return longest_increasing_subsequence_sum


# Test cases
def test_solution():
    func = solution()
    assert func()([1, 2, 3, 4, 5], 9) == 4
    assert func()([4, 3, 2, 1], 10) == 0
    assert func()([1, 5, 2, 9, 3, 7, 4], 15) == 3
    assert func()([1, 2, 3, 4, 5], 15) == 0
    assert func()([1, 3, 5, 2, 4, 6], 12) == 3
    assert func()([1, 1, 1, 1, 1], 5) == 0
    assert func()([10, 5, 20, 15, 30], 45) == 3
    assert func()([1, 2, 3], 6) == 3
    assert func()([1, 2, 3], 7) == 0
    assert func()([10, 22, 9, 33, 21, 50, 41, 60, 80], 133) == 6

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()