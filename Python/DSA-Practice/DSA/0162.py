# DSA Problem 162

'''
Problem Statement:
A palindrome is a number that reads the same backward as forward, such as 121 or 12321. Given a positive integer n, your task is to find the smallest palindrome greater than n that has the same number of digits as n. If no such palindrome exists (for example, if n is 999), return -1.

For instance, if n is 123, the smallest palindrome greater than 123 and having the same number of digits is 131. If n is 99, since there is no 2-digit number greater than 99 and a palindrome, the function should return -1.
'''

Solution:
```python
def next_palindrome(n):
    """
    Finds the smallest palindrome greater than n with the same number of digits.
    If no such palindrome exists, returns -1.
    """
    length = len(str(n))
    start = 10 ** ((length - 1) // 2)
    
    for i in range(start, 10 * start):
        # Generate the first half of the palindrome
        first_half = str(i)
        # Handle even and odd length cases
        if length % 2 == 0:
            palindrome = int(first_half + first_half[::-1])
        else:
            palindrome = int(first_half + first_half[-2::-1])
        
        if palindrome > n:
            return palindrome
    
    return -1

# Check function to test the solution
def check_solution():
    assert next_palindrome(123) == 131, "Test case 1 failed"
    assert next_palindrome(99) == -1, "Test case 2 failed"
    assert next_palindrome(1001) == 1111, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python function `next_palindrome` calculates the next palindrome greater than the input number `n` while maintaining the same number of digits. It iterates through possible first halves of the palindrome, constructs the full palindrome, and checks if it is greater than `n`. The check function `check_solution` is used to verify the correctness of the solution with predefined assertions.