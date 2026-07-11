# DSA Problem 192

'''
Problem Statement:
You are given a list of integers representing the daily temperatures. For each day in the list, you need to find out how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead. Write a function that takes in a list of integers and returns a list where each element is the number of days you would have to wait for a warmer temperature for each day in the input list.

For example, if the input list is [73, 74, 75, 71, 69, 72, 76, 73], the output should be [1, 1, 4, 2, 1, 1, 0, 0] because for the first day (73), the next warmer temperature is on the second day, so you wait 1 day, and so on.
'''

Solution:
def daily_temperatures(temperatures):
    """
    Given a list of daily temperatures, returns a list where each element is the number of days you would have to wait for a warmer temperature.
    """
    answer = [0] * len(temperatures)
    stack = []  # This will store indices of the temperatures list

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)

    return answer

# Function to test the solution with given data points
def check_solution():
    test_temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected_output = [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures(test_temperatures) == expected_output, "Test case failed!"
    print("Test case passed!")

check_solution()