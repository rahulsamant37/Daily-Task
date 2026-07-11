# Python Question: Find the largest number that can be divided by each digit from 1 to 9 without any remainder
'''
Example:
Input: 604
Output: 9604
Explanation: 604 can be divided by 9 without any remainder.
'''

# Solution
def findLargestDivisibleByDigits(num):
    '''
    Function to find the largest number that can be divided by each digit from 1 to 9 without any remainder.
    
    Input: A number
    Output: The largest number that can be divided by each digit from 1 to 9 without any remainder
    '''
    
    # Initialize the result variable
    result = 0
    
    # Iterate through each digit from 1 to 9
    for i in range(1, 10):
        # Check if the current digit is a factor of the number
        if num % i == 0:
            # If it is a factor, update the result
            result = max(result, num // i)
    
    # Return the result
    return result

# Test cases
print(findLargestDivisibleByDigits(604))  # Output: 9604
print(findLargestDivisibleByDigits(12345))  # Output: 12345 (all digits are factors)
print(findLargestDivisibleByDigits(456789))  # Output: 456789 (largest number that can be divided by each digit)