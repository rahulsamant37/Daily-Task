# Python Question: Find the maximum sum of a subset in a given array
'''
Given an integer array, find the maximum sum of a subset of its elements without using any dedicated data structures like Kadane's algorithm or Floyd's Cycle-finding Algorithm.

For example, consider the following array:

Input: [3, -2, 1, -3, 4, -1, 2, 1, -5, 4]

The maximum sum is 10, which can be found by selecting {4, -1, 2, 1} from the array.
'''

# Solution
def maximumSubsetSum(arr):
    n = len(arr)
    
    # base case
    if n == 0:
        return 0
    
    # Initialize the lookup table
    dp = [None] * (n + 1)
    
    # Fill the lookup table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the current element is not present in the subarray, it's the minimum of the subarray and itself
            dp[i] = min(arr[i], dp[i - 1])
            
            # Otherwise, consider the current element with all previous elements
            dp[i] = max(dp[i], dp[i - 1] + arr[i])
    
    # The maximum sum is the last element of the lookup table
    return dp[n]


if __name__ == "__main__":
    arr = [3, -2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('The maximum sum is', maximumSubsetSum(arr))