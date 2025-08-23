# DSA Problem 92

'''
Problem Statement:
Arun has a list of integers representing the daily temperatures over a period. He is interested in finding out how many days he needs to wait until a warmer temperature for each day. If there is no future day for which this is possible, he should put 0 instead. Write a function `days_until_warmer` that takes a list of integers as input and returns a list of integers where each element represents the number of days one has to wait for a warmer temperature compared to the temperature on that day.

Example:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation:
- Day 1 (73) -> Day 2 (74) -> 1 day
- Day 2 (74) -> Day 3 (75) -> 1 day
- Day 3 (75) -> Day 7 (76) -> 4 days
- Day 4 (71) -> Day 6 (72) -> 2 days
- Day 5 (69) -> Day 6 (72) -> 1 day
- Day 6 (72) -> Day 7 (76) -> 1 day
- Day 7 (76) and Day 8 (73) have no future day warmer, so 0 days.
'''

Solution:
```python
def days_until_warmer(temperatures):
    stack = []  # This will store the indices of the temperatures list
    result = [0] * len(temperatures)  # Initialize result array with 0s
    
    for i, temp in enumerate(temperatures):
        # If current temperature is warmer than the temperature at the index stored in stack
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()  # Pop the index of the cooler day
            result[prev_day] = i - prev_day  # Calculate the days until warmer
        stack.append(i)  # Push the current day index onto the stack
    
    return result

# Example check
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(days_until_warmer(temps))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

This solution leverages a stack to keep track of the indices of the temperatures in the list in a way that allows us to efficiently find the number of days until a warmer temperature for each day.