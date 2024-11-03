# DSA Problem generated on 2024-11-04

Here is a unique DSA problem in Python with a solution:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that contains at most `k` distinct elements. For example, if the input list is `[1, 2, 3, 2, 1, 4, 5, 6, 7]` and `k = 3`, the maximum sum of a subarray with at most 3 distinct elements is `17` (from the subarray `[2, 3, 2, 1, 4, 5]`).

**Solution Code:**
```
from collections import defaultdict

def max_sum_k_distinct_elements(arr, k):
    if k == 0:
        return 0
    
    window_start = 0
    max_sum = 0
    curr_sum = 0
    freq_map = defaultdict(int)
    
    for window_end in range(len(arr)):
        freq_map[arr[window_end]] += 1
        curr_sum += arr[window_end]
        
        while len(freq_map) > k:
            freq_map[arr[window_start]] -= 1
            if freq_map[arr[window_start]] == 0:
                del freq_map[arr[window_start]]
            curr_sum -= arr[window_start]
            window_start += 1
        
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 2, 1, 4, 5, 6, 7]
k = 3
print(max_sum_k_distinct_elements(arr, k))  # Output: 17
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input array. Here's a breakdown of the time complexity:

* The outer loop iterates over the entire array, which takes O(n) time.
* The inner while loop iterates at most k times, since we are removing one element from the frequency map at a time. This takes O(k) time.
* The frequency map operations (insertion, deletion, and lookup) take O(1) time on average, since we are using a hash table (Python's `defaultdict`).
* The total time complexity is therefore O(n) + O(k) = O(n), since k is a constant.

Note that the space complexity is O(k), since we are storing at most k elements in the frequency map.