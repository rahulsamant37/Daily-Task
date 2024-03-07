# Python Question: Find the maximum sum in a given array using Kadane's Algorithm
'''
Problem statement: Write a function that takes an integer array as input and returns the maximum sum of a subarray present in the array. If no subarray exists with a positive sum, return 0.

Example:
Input: [1, -3, -5, 2, -1]
Output: 6 (The subarray [2, -1] has a sum of 3)
'''

def max_subarray_sum(arr):
    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

def main():
    arr = [1, -3, -5, 2, -1]
    print("The maximum sum is", max_subarray_sum(arr))

if __name__ == "__main__":
    main()