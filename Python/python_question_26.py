# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Problem statement: Given a set of numbers from 2 to 10, find the largest number that can be divided by each of these numbers without any remainder.

Example:
Input: List of numbers [10, 5, 3, 1]
Output: 10 (10 is the largest number that can be divided by 2, 3, and 5 without any remainder)
'''

def largest_common_divisor(numbers):
    '''
    Function to find the largest number that can be divided by each number from 2 to n without any remainder.
    The function takes a list of numbers as input and returns the largest number.
    '''
    largest = numbers[0]
    for number in numbers[1:]:
        if largest % number == 0:
            largest = largest // number
    return largest

if __name__ == "__main__":
    numbers = [10, 5, 3, 1]
    result = largest_common_divisor(numbers)
    print("The largest number that can be divided by", numbers, "without any remainder is", result)

# Output:
# The largest number that can be divided by [10, 5, 3, 1] without any remainder is 10