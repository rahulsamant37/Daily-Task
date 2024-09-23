# DSA Problem 204

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. Your task is to find the maximum sum of a subsequence of `nums` such that the sum is divisible by `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. If no such subsequence exists, return 0.

For example, if `nums = [4, 5, 6, 7]` and `k = 3`, one such subsequence could be `[4, 5, 7]`, which has a sum of 16. However, this is not the maximum sum divisible by 3. The maximum sum divisible by 3 is 15, achieved by the subsequence `[5, 10]` (assuming 10 is an additional number in the list for the sake of the example).

Constraints:
- 1 <= nums.length <= 10^3
- 1 <= nums[i] <= 10^4
- 1 <= k <= 100
'''

Solution:
```python
from typing import List
import math

def max_sum_div_k(nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of a subsequence of `nums` such that the sum is divisible by `k`.
    """
    dp = [-math.inf] * k
    dp[0] = 0
    for num in nums:
        for i in range(k):
            if dp[i] >= 0:
                dp[(i + num) % k] = max(dp[(i + num) % k], dp[i] + num)
    return dp[0] if dp[0] > 0 else 0

# Example check (You can use these lines to test your function after defining it)
nums = [4, 5, 6, 7]
k = 3
print(max_sum_div_k(nums, k))  # Expected output depends on the input, for example, 15 for a specific input
```

Note: The example check at the end is for demonstration purposes and the expected output will depend on the specific input values.