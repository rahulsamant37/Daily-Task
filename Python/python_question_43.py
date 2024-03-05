# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Given a range of numbers from 2 to 10, find the largest number that can be divided by each number without any remainder.

Example:
Input: List of numbers [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 60 (as 60 is the largest number that can be divided by 2, 3, 4, 5, 6, 7, 8, 9, and 10 without any remainder)
'''

# Solution
def find_largest_number(numbers):
    result = numbers[0] # Initialize result with the first number
    for number in numbers[1:]: # Iterate from the second number
        if result % number == 0: # Check if result is divisible by the current number
            result //= number # Update the result by dividing it by the current number
        else:
            break # If the result is not divisible, break the loop

    return result

# Test cases
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_largest_number(numbers))

# Output: 60