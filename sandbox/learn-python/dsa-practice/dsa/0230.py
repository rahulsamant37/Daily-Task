# DSA Problem 230

'''
Problem Statement:
You are given a list of integers representing the daily temperatures. For each day, you need to find how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0]. This is because for the first temperature 73, you wait 1 day to see a warmer temperature (74), and so on.

Write a function `dailyTemperatures` that takes in a list of integers and returns a list of integers representing the number of days to wait for a warmer temperature.
'''

Solution:
def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # This will store the indices of the temperatures list
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)
    
    return answer

# Example check
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))
# Expected output: [1, 1, 4, 2, 1, 1, 0, 0]
'''
This solution employs a stack to keep track of the indices of the temperatures list for which we haven't found a warmer day yet. As we iterate through the list, we compare each temperature with the temperatures at the indices stored in the stack. If the current temperature is warmer, it means we've found the day for which we've been looking, and we calculate the difference in days (current index - index from stack). The time complexity of this solution is O(n) since each element is pushed and popped from the stack at most once.
'''