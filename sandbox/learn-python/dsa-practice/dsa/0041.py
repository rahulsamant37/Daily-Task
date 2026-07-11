# DSA Problem 41

'''
Problem Statement:
Given a list of integers representing the daily temperatures, return a list where each element indicates the number of days one has to wait for a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures [73, 74, 75, 71, 69, 72, 76, 73], your function should return [1, 1, 4, 2, 1, 1, 0, 0].

Note:
- The length of the input list is in the range [1, 3 * 10^4].
- The values of the temperatures are in the range [30, 100].
'''

Solution:
def daily_temperatures(temps):
    """
    Returns a list where each element represents the number of days one has to wait for a warmer temperature.
    """
    answer = [0] * len(temps)
    stack = []  # Stack to keep track of temperatures and their indices
    
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        stack.append(i)
    
    return answer

# Example check function to verify the solution with provided data points
def check_solution():
    example = [73, 74, 75, 71, 69, 72, 76, 73]
    expected_output = [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures(example) == expected_output, "Test case failed!"
    print("Solution is correct for the given example.")

check_solution()
