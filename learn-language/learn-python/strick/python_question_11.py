# Python Question: Finding the largest number in a list of numbers
'''
Given a list of numbers, find the largest number in the list.

Example:
Input: [3, 10, 20, 50, 100]
Output: 100 (The largest number in the list)
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
        {"numbers": [3, 10, 20, 50, 100], "expected_result": 100},
        {"numbers": [1, 3, 5, 7, 9], "expected_result": 9},
        {"numbers": [10, 20, 30, -20, 50], "expected_result": 50}
    ]
    for data in test_cases:
        numbers = data['numbers']
        result = find_largest_number(numbers)
        if result != data['expected_result']:
            print("Expected:", data['expected_result'])
            print("Actual:", result)

# Main script
if __name__ == "__main__":
    test_find_largest_number()