# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder
'''
Given a range of numbers from 2 to 10, find the largest number that can be evenly divided by all the numbers in the range without any remainder.

Example:

Input: [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 30 (2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 30)
'''

def find_largest_divisible_number(numbers):
    largest_number = numbers[0]
    for number in numbers[1:]:
        if largest_number % number == 0:
            if number > largest_number:
                largest_number = number
    return largest_number

def test_solution():
    assert find_largest_divisible_number([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "Expected result: 30\nGiven result: " + str(find_largest_divisible_number([2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert find_largest_divisible_number([2, 4, 8]) == 8, "Expected result: 8\nGiven result: " + str(find_largest_divisible_number([2, 4, 8]))
    assert find_largest_divisible_number([10, 4, 2, 1]) == 10, "Expected result: 10\nGiven result: " + str(find_largest_divisible_number([10, 4, 2, 1]))
    assert find_largest_divisible_number([1, 2, 3, 5]) == 3, "Expected result: 3\nGiven result: " + str(find_largest_divisible_number([1, 2, 3, 5]))

if __name__ == "__main__":
    test_solution()