# DSA Problem 68

'''
Problem Statement:
You are given an integer array `nums` and an integer `k`. 
Find the total number of continuous subarrays whose sum equals to `k`.

Example:
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: There are two subarrays that sum to 2: [1, 1] at the beginning and [1, 1] at the middle.
'''

Solution:
from collections import defaultdict

def subarraySum(nums, k):
    count, sum_ = 0, 0
    sum_dict = defaultdict(int)
    sum_dict[0] = 1  # To handle the case when sum from the beginning is equal to k
    
    for num in nums:
        sum_ += num
        if sum_ - k in sum_dict:  # Check if there's a subarray (ending at the current index) that sums to k
            count += sum_dict[sum_ - k]
        sum_dict[sum_] += 1  # Record the sum's frequency
    
    return count

# Example usage:
# nums = [1, 1, 1]
# k = 2
# print(subarraySum(nums, k))  # Expected output: 2

'''
Explanation:
This solution uses a hash map (dictionary) to store the cumulative sum up to all the indices possible along with the frequency of the sum. 
It iterates through the list, updating the cumulative sum. For every index, it checks if there's a previous cumulative sum such that 
the difference with the current cumulative sum equals `k`. If such a sum exists, it means there's a subarray that sums to `k`. 
The frequency of such sums is added to the count. This ensures we count all possible subarrays that sum to `k`.
'''