# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Problem statement: Given a set of positive numbers, find the largest number that can be divided without leaving any remainder by all numbers from 2 to the given number.

Example:
Input: {10, 20, 30, 40}
Output: 40 (10 is the largest number that divides all elements without any remainder)
'''

def find_largest_common_divisor(numbers):
    '''
    Function to find the largest common divisor of the given set of numbers
    '''
    largest_divisor = numbers[0]
    for num in numbers[1:]:
        if num > largest_divisor:
            largest_divisor = num
    return largest_divisor

def main():
    '''
    Main function to test the above function
    '''
    numbers = [10, 20, 30, 40]
    result = find_largest_common_divisor(numbers)
    print(result)

if __name__ == "__main__":
    main()

'''
Implement a function that takes in a list of positive integers and returns the largest number that can be divided without any remainder by all numbers from 2 to n (inclusive).
'''