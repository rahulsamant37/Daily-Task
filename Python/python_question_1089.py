# Python Question: Longest Increasing Subsequence with Modifications
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence. However, you are allowed to modify the array at most once. A modification consists of changing the value of a single element in the array to any other integer value.

Example:
Input: nums = [1, 3, 2, 4, 5]
Output: 5
Explanation: Changing 2 to 0 gives [1, 3, 0, 4, 5], and the longest increasing subsequence is [1, 3, 4, 5].
Changing 2 to 6 gives [1, 3, 6, 4, 5], and the longest increasing subsequence is [1, 3, 4, 5].
Changing 3 to 0 gives [1, 0, 2, 4, 5], and the longest increasing subsequence is [1, 2, 4, 5].
Changing 3 to 6 gives [1, 6, 2, 4, 5], and the longest increasing subsequence is [1, 2, 4, 5].
Changing 1 to 0 gives [0, 3, 2, 4, 5], and the longest increasing subsequence is [0, 3, 4, 5].

Input: nums = [5, 4, 3, 2, 1]
Output: 2
Explanation: Change 5 to 0, we have [0, 4, 3, 2, 1]. The LIS is [0, 4] or [0, 3] or [0, 2] or [0, 1]

Input: nums = [1, 2, 3, 4, 5]
Output: 5
Explanation: No need to modify.
'''

# Solution
def solution():
    def longest_increasing_subsequence(arr):
        """
        Finds the length of the longest increasing subsequence in an array.
        Uses dynamic programming to optimize the solution.
        """
        tails = []  # Stores the smallest tail of all increasing subsequences with length i+1 in tails[i].
        for num in arr:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                # Binary search to find the smallest tail that is >= num
                l, r = 0, len(tails) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if tails[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1
                tails[l] = num
        return len(tails)

    def solve(nums):
        n = len(nums)
        max_lis = 0
        for i in range(n):
            original_value = nums[i]

            # Try changing to a very small value
            nums[i] = -10**9 - 1
            max_lis = max(max_lis, longest_increasing_subsequence(nums))

            # Try changing to a very large value
            nums[i] = 10**9 + 1
            max_lis = max(max_lis, longest_increasing_subsequence(nums))

            # Restore the original value
            nums[i] = original_value

        # Also consider the case where no modification is needed
        max_lis = max(max_lis, longest_increasing_subsequence(nums))

        return max_lis

    return solve

# Test cases
def test_solution():
    solve = solution()
    assert solve([1, 3, 2, 4, 5]) == 5
    assert solve([5, 4, 3, 2, 1]) == 2
    assert solve([1, 2, 3, 4, 5]) == 5
    assert solve([1, 5, 2, 4, 3]) == 4
    assert solve([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 8
    assert solve([0, 1, 0, 3, 2, 3]) == 4
    assert solve([7, 7, 7, 7, 7, 7, 7]) == 2
    assert solve([1, 100, 2, 3, 101, 4, 5]) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()