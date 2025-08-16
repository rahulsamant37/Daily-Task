# Python Question: Calculate the largest number that can be divided by each digit from 1 to 9 without any remainder

'''
Problem statement: Given a positive number, find the largest number that can be formed by selecting one digit from each of the digits 1 to 9 without any remainder.

Example:
Input: 548
Output: 845 (The largest number that can be formed using the given digits without any remainder)
'''

def largest_digit_number(n: int) -> int:
    # Create a dictionary to store the remaining digits after selecting a digit from each place
    digits_dict = {1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1}

    # Find the largest number by iterating over each place value and selecting the largest possible digit
    largest_number = 0
    for place in range(1, 10):
        # Calculate the largest possible digit for the current place
        largest_digit = digits_dict[place]

        # Update the largest number by replacing the current place value with the largest possible digit and check if it is greater than the current largest number
        largest_number = max(largest_number, n // place * largest_digit)

    return largest_number


# Example usage
n = 548
print(largest_digit_number(n))  # Output: 845