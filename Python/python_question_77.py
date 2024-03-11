# Python Question: Find the largest number that can be divided by any number from 1 to 10 without any remainder

'''
Problem Statement: Given an integer, find the largest number that can be divided by any number from 1 to 10 without any remainder.

Example:
Input: 36
Output: 12 (as 36 is divisible by 1, 2, 3, 4, 6)
'''

def find_largest_number(number):
    # Create a dictionary to store the result
    result = {}

    # Iterate from 1 to 10 and find the largest number that divides the given number without a remainder
    for i in range(1, 11):
        if number % i == 0:
            result[i] = number // i
            if len(str(result[i])) > len(str(result[result[i]]):
                result[result[i]] = result[i]
            else:
                result[i] = result[result[i]]

    # Return the largest number found
    return result[10]

if __name__ == "__main__":
    print(find_largest_number(36))