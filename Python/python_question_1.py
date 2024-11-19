# Python Question: Find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder

'''
Find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder.

Example:
Input: list of numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: largest_number = 120 (60 minutes x 2 hours)
'''

def largest_number(numbers):
    '''
    This function will find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder.
    '''
    largest_number = 1
    for num in numbers:
        if num > largest_number:
            largest_number = num
    return largest_number

def test_largest_number():
    '''
    This function tests the largest_number function with sample numbers and verifies the result.
    '''
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert largest_number(numbers) == 120, "Test failed. Expected result: 120, Actual result: " + str(largest_number(numbers))

if __name__ == "__main__":
    test_largest_number()

'''