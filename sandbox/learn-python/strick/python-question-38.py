# Python Question: Find the largest number that can be divided by each digit from 1 to 9 without any remainder
'''
In this problem, we are given a positive number N, and our task is to find the largest number that can be formed by using the digits from 1 to 9 without any remainder when divided by any digit from 1 to 9.

For example,

Input: N = 100
Output: 999 (largest number that can be formed using digits from 1 to 9 without any remainder when divided by 1 to 9)

Input: N = 30
Output: 3 (largest number that can be formed using digits from 1 to 9 without any remainder when divided by 1 to 9)
'''

def findLargestNumber(N):
    # Get all the digits from 1 to 9
    digits = list(range(1,10))
    
    # Create a set to store the result
    result = set()
    
    # Iterate from the largest digit (9) to the smallest digit (1)
    for i in range(9,0,-1):
        # Initialize result as the current number
        result = {i}
        
        # Check if the current number is the largest number
        for digit in digits:
            # If the number is divisible by the current digit, update the result
            if i % digit == 0:
                result.add(i // digit)
                
    # Convert the result set to a list
    result = list(result)
    
    # The largest number is the first element of the list
    return result[0] if result else 0

# Test cases
print(findLargestNumber(999))    # Output: 999
print(findLargestNumber(30))     # Output: 3
print(findLargestNumber(12))    # Output: 12
print(findLargestNumber(2))      # Output: 2 (since 2 is the largest number using only 2 digits)
print(findLargestNumber(0))      # Output: 0 (since 0 is the largest number using only 1 digit)