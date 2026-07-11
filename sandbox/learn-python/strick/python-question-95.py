# Python Question: Find the maximum sum subarray within a given array
'''
Given an integer array, find a subarray with the maximum sum. If such a subarray exists within the given array, return it. If not, return an empty list.

For example, consider the following array:
Input: [1, 2, 3, 5, 7, 8, 9]
Output: [5, 7, 8, 9]

Input: [1, -3, -5, -7]
Output: []
'''

def max_sum_subarray(arr):
    # Base case: If the length of the array is 0 or 1, return the array itself
    if len(arr) <= 1:
        return arr

    # Initialize the maximum sum and the current sum
    max_sum = sum = arr[0]

    for i in range(1, len(arr)):
        # Update the current sum with the negative value and add the positive value
        curr_sum = sum = max(arr[i], 0) + arr[i]

        # Update the maximum sum if the current sum is greater
        if curr_sum > max_sum:
            max_sum = curr_sum

        # Update the sum if the current sum is smaller than the previous sum
        if sum < curr_sum:
            sum = curr_sum

    return max_sum


if __name__ == "__main__":
    arr = [1, -3, -5, -7, 2, -1, -2, 4]
    print(max_sum_subarray(arr))