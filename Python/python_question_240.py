# Python Question: Find the Largest Sum Contiguous Subarray with at Least K Elements
'''
Given an array of integers `arr` and an integer `k`, find the contiguous subarray of size at least `k` that has the largest sum. Return this largest sum.

Example:
Input: arr = [1, 3, -2, 5, 4], k = 3
Output: 12
Explanation: The subarray [3, -2, 5, 4] has the largest sum of 10. The subarray [1, 3, -2, 5, 4] has the largest sum of 11. The subarray [3, -2, 5] has a sum of 6. The subarray [-2, 5, 4] has a sum of 7. The largest sum is 1 + 3 + (-2) + 5 + 4 = 11. The subarray [3, -2, 5, 4] has sum 10. The subarray [5, 4] is smaller than k=3. The subarray [3, -2, 5] has sum 6. The subarray [5, 4] is smaller than k=3.
The subarray [1, 3, -2, 5, 4] has sum 11. The subarray [3, -2, 5, 4] has sum 10. The subarray [-2, 5, 4] has sum 7.
The subarray [1, 3, -2] has sum 2. The subarray [3, -2, 5] has sum 6. The subarray [-2, 5, 4] has sum 7. The subarray [5, 4] has sum 9.
The subarray [1, 3, -2, 5] has sum 7. The subarray [3, -2, 5, 4] has sum 10.
The subarray [1, 3, -2, 5, 4] has sum 11.

Input: arr = [-1, -2, 3, -4, 5], k = 2
Output: 5
Explanation: The subarray [5] has the largest sum of 5. The subarray [-4, 5] has sum of 1. The subarray [3, -4, 5] has sum 4. The subarray [-2, 3, -4, 5] has sum 2. The subarray [-1, -2, 3, -4, 5] has sum 1.

'''

# Solution
def solution():
    def largest_sum_subarray_k(arr, k):
        """
        Finds the largest sum contiguous subarray of size at least k.

        Args:
            arr: A list of integers.
            k: The minimum size of the subarray.

        Returns:
            The largest sum of a contiguous subarray of size at least k.
        """
        n = len(arr)
        if n < k:
            return float('-inf')  # Handle cases where array size is less than k

        # Calculate the sum of the first k elements
        current_sum = sum(arr[:k])
        max_sum = current_sum

        # Iterate from k to n
        for i in range(k, n):
            current_sum += arr[i] - arr[i - k]  # Sliding window approach
            max_sum = max(max_sum, current_sum)

        # Iterate through the array to find subarrays larger than k
        for i in range(k, n):
            current_max = arr[i]
            temp_sum = arr[i]
            for j in range(i - 1, -1, -1):
                temp_sum += arr[j]
                if (i - j + 1) >= k:
                    current_max = max(current_max, temp_sum)
            max_sum = max(max_sum, current_max)
        
        # Kadane's Algorithm with Minimum Length Constraint
        max_so_far = float('-inf')
        current_max = 0
        start_index = 0
        best_start_index = 0
        best_end_index = -1

        for i in range(n):
            if current_max == 0:
                start_index = i

            current_max += arr[i]

            if current_max > max_so_far:
                max_so_far = current_max
                best_start_index = start_index
                best_end_index = i

            if current_max < 0:
                current_max = 0

        # Check if the length of the best subarray is at least k
        if best_end_index - best_start_index + 1 < k:
            # Iterate to find a valid subarray with length >= k
             max_so_far = float('-inf')
             for i in range(n - k + 1):
                 current_sum = sum(arr[i:i+k])
                 max_so_far = max(max_so_far, current_sum)
                 for j in range(i+k, n):
                     current_sum += arr[j]
                     max_so_far = max(max_so_far, current_sum)
             return max_so_far


        # Expand the best subarray to satisfy the k elements constraint
        final_max_sum = float('-inf')
        for i in range(best_start_index, best_end_index - k + 2):
            current_sum = 0
            for j in range(i, best_end_index + 1):
                current_sum += arr[j]
                if j - i + 1 >= k:
                    final_max_sum = max(final_max_sum, current_sum)
        return final_max_sum

    return largest_sum_subarray_k

# Test cases
def test_solution():
    arr1 = [1, 3, -2, 5, 4]
    k1 = 3
    expected1 = 12
    assert solution()(arr1, k1) == expected1

    arr2 = [-1, -2, 3, -4, 5]
    k2 = 2
    expected2 = 5
    assert solution()(arr2, k2) == expected2

    arr3 = [1, 1, 1, 1, 1]
    k3 = 2
    expected3 = 5
    assert solution()(arr3, k3) == expected3

    arr4 = [-1, -1, -1]
    k4 = 2
    expected4 = -2
    assert solution()(arr4, k4) == -2

    arr5 = [1, 2, 3]
    k5 = 1
    expected5 = 6
    assert solution()(arr5, k5) == 6

    arr6 = [-5, 8, -10, 4, 9, -3, 2, 1]
    k6 = 3
    expected6 = 15
    assert solution()(arr6, k6) == 15

    arr7 = [-4, -2, 1, -3]
    k7 = 2
    expected7 = -1
    assert solution()(arr7, k7) == -1

    arr8 = [10, -1, -2, 3, 4, -5, 6]
    k8 = 4
    expected8 = 10
    assert solution()(arr8, k8) == 10

    arr9 = [-10, -1, -2, -3, -4, -5, -6]
    k9 = 3
    expected9 = -6
    assert solution()(arr9, k9) == -6

    arr10 = [1,2,3,4,5,6]
    k10 = 4
    expected10 = 15
    assert solution()(arr10, k10) == 20

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()