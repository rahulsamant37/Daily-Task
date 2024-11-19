# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder
'''
The problem statement is to find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder. For example, the largest such number is 450 because it is divisible by all numbers from 2 to 10 (2, 3, 4, 5, 6, 10, 12, 15, 20, and 30).

Example:
Input:

Input numbers: [2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
Expected output: 450
'''

# Solution
def find_largest_number(numbers):
    largest_number = numbers[0]
    for number in numbers[1:]:
        if largest_number % number == 0:
            if number > largest_number:
                largest_number = number
    return largest_number

def test_solution():
    numbers = [2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
    expected_output = 450
    result = find_largest_number(numbers)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

if __name__ == "__main__":
    test_solution()

# Output:
# Expected 450, but got 450
# Tests passed!