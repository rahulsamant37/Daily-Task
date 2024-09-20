# DSA Problem 201

'''
Problem Statement:
You are given a list of integers representing the daily temperatures. Your task is to create a function `daily_temp_wait` that, for each day in the input list, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list [73, 74, 75, 71, 69, 72, 76, 73], your function should return [1, 1, 4, 2, 1, 1, 0, 0].

Constraints:
- The length of the temperatures list will be in the range [1, 30000].
- Each temperature will be an integer in the range [30, 100].
'''

Solution:
```python
def daily_temp_wait(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # To store indices of the temperatures list
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)
    
    return answer

# Example check
print(daily_temp_wait([73, 74, 75, 71, 69, 72, 76, 73]))  # Output should be [1, 1, 4, 2, 1, 1, 0, 0]
```

This solution uses a stack to keep track of the indices for which we haven't yet found a warmer day. As we iterate through the list, we check if the current day's temperature is warmer than the last index in the stack. If it is, we calculate the difference and update the answer list for that index. This approach ensures that we only go through the list once, making it efficient.