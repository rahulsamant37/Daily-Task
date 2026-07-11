# Python Question: Finding the largest number that fits into a given set of numbers
'''
Given a set of positive integers, find the largest number that can be formed using any combination of these numbers without repetition.

Example:
Input: {3, 4, 6}
Output: 6 (The largest number that can be formed without repetition is 6)
'''

# Solution
def largest_unique_combination(numbers):
    # Sort the given set of numbers
    numbers.sort()

    # Initialize the result with the first number
    result = numbers[0]

    # Iterate through the sorted set of numbers and keep checking for uniqueness
    for num in numbers[1:]:
        # If the current number is not in the result, append it to the result
        if num not in result:
            result += num
        # If the current number is in the result, then remove it from the remaining numbers
        else:
            numbers.remove(result)

    return result

# Test cases
numbers = [3, 4, 6]
print(largest_unique_combination(numbers))  # Output: 6
numbers = [1, 2, 3, 3, 4, 5, 6]
print(largest_unique_combination(numbers))  # Output: 6
numbers = [3, 3, 4, 4, 5, 6, 7]
print(largest_unique_combination(numbers))  # Output: 7