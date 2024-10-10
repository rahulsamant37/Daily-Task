# DSA Problem for 2024-10-11

Here is a novel DSA problem with a Python solution for 2024-10-11:

**Problem Statement:**

**Largest Subarray with At Most K Distinct Characters**

Given an array of integers `arr` and an integer `k`, find the largest subarray that contains at most `k` distinct characters.

**Example:**

Input: `arr = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9], k = 3`
Output: `[2, 3, 2, 1, 4, 5, 6]`

**Optimal Solution:**
```python
def largest_subarray_with_k_distinct(arr, k):
    from collections import defaultdict
    char_freq = defaultdict(int)
    left = 0
    max_len = 0
    max_subarray = []
    for right, num in enumerate(arr):
        char_freq[num] += 1
        while len(char_freq) > k:
            char_freq[arr[left]] -= 1
            if char_freq[arr[left]] == 0:
                del char_freq[arr[left]]
            left += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_subarray = arr[left:right+1]
    return max_subarray
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n), where n is the length of the input array `arr`. The algorithm iterates through the array once, and the while loop inside the for loop iterates at most n times in the worst case.
* Space complexity: O(min(n, k)), where k is the number of distinct characters in the input array. The `char_freq` dictionary stores at most k elements, and the `max_subarray` list stores at most n elements.

**Explanation:**

The algorithm uses a sliding window approach to find the largest subarray with at most k distinct characters. The `char_freq` dictionary keeps track of the frequency of each character in the current window. The `left` variable marks the start of the window, and the `right` variable marks the end of the window.

When the number of distinct characters in the window exceeds k, the algorithm slides the window to the right by incrementing the `left` variable and decrementing the frequency of the character at the `left` index. If the frequency becomes 0, the character is removed from the `char_freq` dictionary.

The algorithm keeps track of the maximum length of the subarray and the corresponding subarray using the `max_len` and `max_subarray` variables.

Finally, the algorithm returns the largest subarray with at most k distinct characters.