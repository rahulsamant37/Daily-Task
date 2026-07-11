# Python Question: Calculate the largest number possible with a limited set of digits
'''
Problem statement: Given a set of digits (0-9), find the largest number possible that can be formed by any combination of these digits.

Example:
Input: {2, 4, 6}
Output: 642 (The largest number possible from the given set)
'''

def solution(digits):
    # Sort the given set of digits
    sorted_digits = sorted(digits)

    # Initialize the largest number as the first element of the sorted set
    largest_number = sorted_digits[0]

    # Iterate through the sorted set and update the largest number if a larger number is found
    for digit in sorted_digits:
        if int(largest_number) + str(digit) > int(digit) + str(largest_number):
            largest_number = digit

    return largest_number

def test_solution():
    test_case1 = [2, 4, 6]
    assert solution(test_case1) == 642, "Test case 1 failed."

    test_case2 = [9, 8, 7]
    assert solution(test_case2) == 897, "Test case 2 failed."

    test_case3 = [1, 0, 9]
    assert solution(test_case3) == 910, "Test case 3 failed."

test_solution()