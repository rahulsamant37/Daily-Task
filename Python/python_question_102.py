# Python Question: Find the largest number that can be divided by any number from 1 to 10 without any remainder

'''
The problem statement is to find the largest number that can be divided by any number from 1 to 10 without any remainder.

Example:
Input: 100
Output: 50 (Since 50 is divisible by all numbers from 1 to 10 without any remainder)
'''

# Solution
def largestDivisibleBy(number):
    '''
    This function takes a number as input and checks if it is divisible by numbers from 1 to 10 or not.
    It returns the largest number that is divisible by all numbers from 1 to 10.
    '''
    # Create a set of numbers from 1 to 10
    numbers = set(range(1, 11))
    
    # Check if current number is divisible by each number in the set
    for i in numbers:
        if number % i == 0:
            # If the number is divisible by all numbers in the set, return it
            if len(numbers - {i}) == 0:
                return number
    
    # If the number is not divisible by any number in the set, return the number itself
    return number

if __name__ == "__main__":
    largest_number = largestDivisibleBy(100)
    print("The largest number that is divisible by numbers from 1 to 10 is", largest_number)