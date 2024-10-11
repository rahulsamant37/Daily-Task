# DSA Problem 222

'''
Problem Statement:
You are given a list of integers representing the daily temperatures. Design an algorithm to return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note that the input list temperatures will have at least 1 day and at most 30000 days, and each temperature will be an integer in the range [30, 100].
'''

Solution:
def daily_temperatures(temps):
    """
    Given a list of daily temperatures, returns a list where each element is the number of days
    until a warmer temperature. If there is no future day for which this is possible, returns 0.
    """
    answer = [0] * len(temps)
    stack = []  # Stack to keep track of temperatures and their indices
    
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)
    
    return answer

# Example usage
if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temperatures))
    # Expected output: [1, 1, 4, 2, 1, 1, 0, 0]

This solution uses a stack to keep track of the temperatures and their indices. As we iterate through the list, if the current temperature is warmer than the temperature at the index stored at the top of the stack, we calculate the difference in days and update the answer list. This allows us to efficiently find the number of days until a warmer temperature for each day in the input list.