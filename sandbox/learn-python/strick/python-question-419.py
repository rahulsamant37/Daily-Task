# Python Question: Find the Longest Increasing Subsequence with Maximum Sum
'''
Given an array of integers, find the longest increasing subsequence (LIS) such that the sum of its elements is maximum. If there are multiple LIS with the same length, return the one with the maximum sum.

Input: [1, 101, 2, 3, 100, 4, 5]
Output: [1, 2, 3, 100] (Length: 4, Sum: 106)

Input: [10, 5, 4, 3]
Output: [10] (Length: 1, Sum: 10)

Input: [3, 4, 5, 10]
Output: [3, 4, 5, 10] (Length: 4, Sum: 22)
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_max_sum(arr):
        """
        Finds the longest increasing subsequence (LIS) with the maximum sum.

        Args:
          arr: A list of integers.

        Returns:
          A list representing the LIS with the maximum sum.
        """

        n = len(arr)

        # lis_lengths[i] stores the length of the LIS ending at arr[i]
        lis_lengths = [1] * n

        # lis_sums[i] stores the sum of the LIS ending at arr[i]
        lis_sums = [arr[i] for i in range(n)]

        # predecessors[i] stores the index of the predecessor of arr[i] in the LIS
        predecessors = [i for i in range(n)]

        # Iterate through the array to build the LIS lengths and sums
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    # If we can extend the LIS ending at arr[j] with arr[i]
                    if lis_lengths[i] < lis_lengths[j] + 1:
                        # If the new LIS is longer, update the length, sum, and predecessor
                        lis_lengths[i] = lis_lengths[j] + 1
                        lis_sums[i] = lis_sums[j] + arr[i]
                        predecessors[i] = j
                    elif lis_lengths[i] == lis_lengths[j] + 1 and lis_sums[i] < lis_sums[j] + arr[i]:
                        # If the new LIS has the same length but a larger sum, update the sum and predecessor
                        lis_sums[i] = lis_sums[j] + arr[i]
                        predecessors[i] = j

        # Find the index of the LIS with the maximum length and sum
        max_len = max(lis_lengths)
        max_sum = float('-inf')
        max_index = -1

        for i in range(n):
            if lis_lengths[i] == max_len and lis_sums[i] > max_sum:
                max_sum = lis_sums[i]
                max_index = i

        # Reconstruct the LIS from the predecessor array
        lis = []
        current = max_index
        while current != predecessors[current]:
            lis.append(arr[current])
            current = predecessors[current]
        lis.append(arr[current])

        return lis[::-1]  # Reverse the list to get the correct order
    return longest_increasing_subsequence_with_max_sum

# Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            raise AssertionError(f"Test failed: {message} Expected {expected}, but got {actual}")
        else:
            print(f"Test passed: Actual {actual} == Expected {expected}")

    lis_func = solution()

    # Test case 1
    arr1 = [1, 101, 2, 3, 100, 4, 5]
    expected1 = [1, 2, 3, 100]
    assert_equal(lis_func(arr1), expected1, "Test Case 1 Failed")

    # Test case 2
    arr2 = [10, 5, 4, 3]
    expected2 = [10]
    assert_equal(lis_func(arr2), expected2, "Test Case 2 Failed")

    # Test case 3
    arr3 = [3, 4, 5, 10]
    expected3 = [3, 4, 5, 10]
    assert_equal(lis_func(arr3), expected3, "Test Case 3 Failed")

    # Test case 4
    arr4 = [1, 2, 3, 4, 5]
    expected4 = [1, 2, 3, 4, 5]
    assert_equal(lis_func(arr4), expected4, "Test Case 4 Failed")

    # Test case 5
    arr5 = [5, 4, 3, 2, 1]
    expected5 = [5]
    assert_equal(lis_func(arr5), expected5, "Test Case 5 Failed")

    # Test case 6
    arr6 = [1, 3, 2, 4, 5]
    expected6 = [1, 2, 4, 5]
    assert_equal(lis_func(arr6), [1, 3, 4, 5], "Test Case 6 Failed")

    # Test case 7 - Duplicate values
    arr7 = [1, 2, 2, 3]
    expected7 = [1, 2, 3]
    assert_equal(lis_func(arr7), [1, 2, 3], "Test Case 7 Failed")

    # Test case 8 - Empty array
    arr8 = []
    expected8 = []
    assert_equal(lis_func(arr8), [], "Test Case 8 Failed")

    # Test case 9 - Single element array
    arr9 = [5]
    expected9 = [5]
    assert_equal(lis_func(arr9), [5], "Test Case 9 Failed")

if __name__ == "__main__":
    test_solution()