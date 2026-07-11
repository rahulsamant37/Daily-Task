# DSA Problem 115

'''
Problem Statement:
You are given a list of positive integers, `nums`. Your task is to find the minimum number of swaps required to sort the list in non-decreasing order. In one swap, you can choose any two elements from the list and swap their positions. If the list is already sorted, the number of swaps required is 0.

Constraints:
- 1 <= len(nums) <= 10^3
- 1 <= nums[i] <= 10^6

Example:
Input: nums = [4, 3, 2, 1]
Output: 2
Explanation: You can sort the array in 2 swaps. One way to do this is to swap (4, 1) and (3, 2).
'''

Solution:
```python
def min_swaps_to_sort(nums):
    n = len(nums)
    arr_pos = [*enumerate(nums)]
    arr_pos.sort(key=lambda it: it[1])
    vis = {i: False for i in range(n)}
    ans = 0

    for i in range(n):
        if vis[i] or arr_pos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

# Example usage
nums = [4, 3, 2, 1]
print(min_swaps_to_sort(nums))  # Output: 2
```

Explanation:
This solution works by first associating the value of each element with its index and then sorting the array by value. It then determines the number of swaps needed by calculating the length of cycles in the permutation of indices required to sort the array. The number of swaps for a cycle of length `L` is `L - 1`. The overall number of swaps needed to sort the entire array is the sum of the number of swaps needed for each cycle.