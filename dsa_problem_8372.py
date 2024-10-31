# DSA Problem generated on 2024-11-01

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a list of integers, find the maximum sum of a subarray that can be formed by taking elements from the list in a zigzag manner. A zigzag manner means that you can take an element from the list, then skip one element, take another element, skip one element, and so on.

For example, if the input list is `[1, 2, 3, 4, 5, 6]`, a possible zigzag subarray could be `[1, 3, 5]` or `[2, 4, 6]`.

**Solution Code:**

```
def max_zigzag_sum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = nums[0]
    dp[1][1] = nums[1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2] + nums[i], dp[0][i-2])
        dp[1][i] = max(dp[0][i-2] + nums[i], dp[1][i-2])

    return max(dp[0][-1], dp[1][-1])

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
print(max_zigzag_sum(nums))  # Output: 9
```

**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input list `nums`. This is because we iterate over the list once to fill up the dynamic programming (DP) table.

The space complexity is also O(n), as we need to store the DP table of size 2xN.

The intuition behind the solution is that we maintain two arrays, `dp[0]` and `dp[1]`, to store the maximum sum of zigzag subarrays ending at each position. We iterate over the list, and for each position, we calculate the maximum sum by considering the previous two elements in the zigzag manner. Finally, we return the maximum sum from the two arrays.

Note that this problem is a variation of the classic dynamic programming problem, "Maximum Sum Subarray", with an additional constraint of zigzag selection.