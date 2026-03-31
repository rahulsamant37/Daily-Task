# Python Question: Find the Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers `nums`, find the longest increasing subsequence (LIS) such that the sum of its elements is maximized. Return the maximum sum.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

An increasing subsequence is a subsequence in which the elements are in strictly increasing order.

Example:
Input: nums = [1, 101, 2, 3, 100, 4, 5]
Output: 106
Explanation: The longest increasing subsequence with maximum sum is [1, 2, 3, 100], which has a sum of 106.

Input: nums = [10, 5, 4, 3]
Output: 10
Explanation: The longest increasing subsequence with maximum sum is [10], which has a sum of 10.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_max_sum(nums):
        """
        Finds the longest increasing subsequence with maximum sum in the given array.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of the longest increasing subsequence.
        """

        n = len(nums)
        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        # sums[i] is the sum of elements in the longest increasing subsequences with length i+1 ending at tails[i].
        tails = []
        sums = []

        for num in nums:
            if not tails or num > tails[-1]:
                # Extend the longest increasing subsequence.
                if not tails:
                  prev_sum = 0
                else:
                  prev_sum = sums[-1]

                tails.append(num)
                sums.append(prev_sum + num)
            else:
                # Find the smallest tail that is >= num and replace it with num.
                l, r = 0, len(tails) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if tails[mid] < num:
                        l = mid + 1
                    else:
                        r = mid - 1

                # Replace tails[l] with num.
                tails[l] = num
                
                #Update the sums[l]
                if l == 0:
                    sums[l] = num
                else:
                    sums[l] = sums[l-1] + num

        return sums[-1] if sums else 0

    return longest_increasing_subsequence_with_max_sum


# Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            print(f"Assertion failed: {message}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")
            raise AssertionError
    
    nums1 = [1, 101, 2, 3, 100, 4, 5]
    assert_equal(solution()(nums1), 106, "Test Case 1 Failed")

    nums2 = [10, 5, 4, 3]
    assert_equal(solution()(nums2), 10, "Test Case 2 Failed")

    nums3 = [3, 2, 6, 4, 5, 1]
    assert_equal(solution()([10, 22, 9, 33, 21, 50, 41, 60, 80]), 263, "Test Case 3 Failed")

    nums4 = [1, 2, 3, 4, 5]
    assert_equal(solution()(nums4), 15, "Test Case 4 Failed")

    nums5 = [5, 4, 3, 2, 1]
    assert_equal(solution()(nums5), 5, "Test Case 5 Failed")

    nums6 = [1]
    assert_equal(solution()([10]), 10, "Test Case 6 Failed")

    nums7 = []
    assert_equal(solution()([]), 0, "Test Case 7 Failed")

    nums8 = [1, 3, 2, 4, 5]
    assert_equal(solution()(nums8), 15, "Test Case 8 Failed")

    nums9 = [4, 2, 3, 7, 2, 1, 8, 6]
    assert_equal(solution()([4, 2, 3, 7, 2, 1, 8, 6]), 28, "Test Case 9 Failed")

    nums10 = [8, 4, 2, 10, 6, 14, 1, 9, 5, 13]
    assert_equal(solution()([8, 4, 2, 10, 6, 14, 1, 9, 5, 13]), 54, "Test Case 10 Failed")

if __name__ == "__main__":
    test_solution()