# Python Question: Largest Sum Contiguous Subarray with at least K elements
'''
Given an array of integers `arr` and an integer `k`, find the contiguous subarray of size at least `k` that has the largest sum. Return the largest sum.

Example:
Input: arr = [1, 2, 3, 4, 5, 6], k = 3
Output: 20
Explanation: The subarray [2, 3, 4, 5, 6] has the largest sum of 20 and has a length of at least 3.

Input: arr = [-1, -2, 1, 2, 3, -4, 5], k = 2
Output: 6
Explanation: The subarray [1, 2, 3] has the largest sum of 6 and has a length of at least 2.

Input: arr = [1, 1, 1, 1, 1, 1], k = 2
Output: 6
'''

# Solution
def solution():
    def largest_sum_subarray_k(arr, k):
        """
        Finds the largest sum contiguous subarray of size at least k.

        Args:
            arr: The input array of integers.
            k: The minimum size of the subarray.

        Returns:
            The largest sum of a contiguous subarray of size at least k.
        """

        n = len(arr)
        if n < k:
            return -float('inf')  # Or raise an exception if you prefer

        # Calculate the sum of the first k elements
        current_sum = sum(arr[:k])
        max_sum = current_sum

        # Iterate through the remaining elements
        for i in range(k, n):
            current_sum += arr[i] - arr[i - k]  # Slide the window of size k
            max_sum = max(max_sum, current_sum)  # Update max_sum with the current window's sum

            # Now, consider subarrays larger than k
            temp_sum = current_sum
            for j in range(i - k, -1, -1):
                temp_sum += arr[j]
                max_sum = max(max_sum, temp_sum)

        return max_sum

    return largest_sum_subarray_k

# Test cases
def test_solution():
    largest_sum_subarray_k = solution()

    # Test case 1
    arr1 = [1, 2, 3, 4, 5, 6]
    k1 = 3
    expected1 = 20
    assert largest_sum_subarray_k(arr1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {largest_sum_subarray_k(arr1, k1)}"

    # Test case 2
    arr2 = [-1, -2, 1, 2, 3, -4, 5]
    k2 = 2
    expected2 = 6
    assert largest_sum_subarray_k(arr2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {largest_sum_subarray_k(arr2, k2)}"

    # Test case 3
    arr3 = [1, 1, 1, 1, 1, 1]
    k3 = 2
    expected3 = 6
    assert largest_sum_subarray_k(arr3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {largest_sum_subarray_k(arr3, k3)}"

    # Test case 4
    arr4 = [-1, -2, -3]
    k4 = 1
    expected4 = -1
    assert largest_sum_subarray_k(arr4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {largest_sum_subarray_k(arr4, k4)}"

    # Test case 5
    arr5 = [1, 2, -3, 4, -5, 6]
    k5 = 3
    expected5 = 6
    assert largest_sum_subarray_k(arr5, k5) == 6, f"Test Case 5 Failed: Expected {6}, Got {largest_sum_subarray_k(arr5, k5)}"

    # Test case 6: k is larger than the array
    arr6 = [1, 2]
    k6 = 3
    expected6 = -float('inf')
    assert largest_sum_subarray_k(arr6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {largest_sum_subarray_k(arr6, k6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()