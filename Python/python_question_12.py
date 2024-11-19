# Python Question: Finding the largest number in a list of integers

'''
Given a list of integers, find the largest number in the list.

Example:
Input: [10, 20, 30, 40, 50]
Output: 50
'''

# Solution
def find_largest_number(numbers):
    largest_number = numbers[0]
    for num in numbers:
        if num > largest_number:
            largest_number = num
    return largest_number

# Test cases
def test_find_largest_number():
    test_cases = [
        {"numbers": [10, 20, 30, 40, 50], "expected_result": 50},
        {"numbers": [1, 2, 3, 4, 5], "expected_result": 5},
        {"numbers": [100, 999, -10, 0], "expected_result": 999},
        {"numbers": [], "expected_result": None}
    ]
    for test_case in test_cases:
        numbers = test_case["numbers"]
        result = find_largest_number(numbers)
        if result != test_case["expected_result"]:
            print(f"Error: Incorrect result for input {numbers}, expected {test_case['expected_result']}, but got {result}")

test_find_largest_number()