# DSA Problem 160

'''
Problem Statement:
You are given a list of integers representing the daily temperatures. For each day, you need to find out how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead. For example, if the input is [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0] because on the first day, the next warmer temperature is on the second day, and so on.
'''

Solution:
def daily_temperatures(T):
    """
    Given a list of daily temperatures, returns a list where each element is the number of days
    one must wait for a warmer temperature. If no warmer temperature is coming, the value is 0.
    """
    answer = [0] * len(T)
    stack = []  # This will store indices of the temperatures list

    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            answer[cur] = i - cur
        stack.append(i)
    
    return answer

# Example check function to verify the solution with provided data points
def check_solution():
    test_cases = [[73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60], [30]]
    expected_outputs = [[1, 1, 4, 2, 1, 1, 0, 0], [1, 1, 1, 0], [0]]
    for i, test_case in enumerate(test_cases):
        result = daily_temperatures(test_case)
        assert result == expected_outputs[i], f"Test case {i+1} failed. Expected {expected_outputs[i]}, got {result}"
    print("All test cases passed.")

check_solution()
