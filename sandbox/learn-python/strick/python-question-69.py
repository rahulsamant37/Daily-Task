# Python Question: Find the largest number that can be divided by any number from 1 to 10 without any remainder

'''
Problem statement: Given a list of integers, find the largest number that can be divided by any number from the given list without any remainder.

Example:
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 9 (as 9 can be divided by all numbers from 1 to 10 without any remainder)
'''

def find_largest_divisible_number(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)

    # Find the last number of the sorted list
    largest_num = numbers[0]

    # Iterate through numbers from 1 to largest_num
    for i in range(1, largest_num+1):
        # Check if the current number is a multiple of the largest number
        if i % largest_num == 0:
            # If the current number is a multiple of the largest number, update the largest number
            largest_num = i

    return largest_num

# Test cases
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Largest number divisible by numbers from 1 to 10 is:", find_largest_divisible_number(numbers))

numbers = [10, 5, 3, 2, 1]
print("Largest number divisible by numbers from given list is:", find_largest_divisible_number(numbers))