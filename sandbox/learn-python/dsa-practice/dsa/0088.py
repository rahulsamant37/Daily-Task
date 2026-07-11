# DSA Problem 88

'''
Problem Statement:
Given a list of integers `nums`, and an integer `k`, find the number of unique pairs `(nums[i], nums[j])` such that the absolute difference between `nums[i]` and `nums[j]` is exactly `k`, and `i` is not equal to `j`.

Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2] and [2,1] when considering the first and second elements.
- [1,2] and [2,1] when considering the first and third elements.
- [2,1] and [1,2] when considering the second and fourth elements.
- [2,1] and [1,2] when considering the third and fourth elements.

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Constraints:
- 2 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^9
- 0 <= k <= 10^9
'''

Solution:
```python
def count_unique_pairs(nums, k):
    from collections import Counter
    
    # Count the frequency of each number in nums
    freq = Counter(nums)
    
    count = 0
    for num in freq:
        if k > 0 and (num + k) in freq:
            count += freq[num] * freq[num + k]
        elif k == 0 and freq[num] > 1:
            count += freq[num] * (freq[num] - 1)
    
    return count

# Example check function (not part of the solution)
def check_solution():
    assert count_unique_pairs([1,2,2,1], 1) == 4
    assert count_unique_pairs([1,3], 3) == 0
    print("All tests passed!")

check_solution()
```
This solution uses a `Counter` from the `collections` module to quickly count the occurrences of each number in the list. It then iterates through each unique number, checking whether the sum of that number and `k` is also present in the list. If `k` is 0, it checks whether the number appears more than once to form valid pairs.