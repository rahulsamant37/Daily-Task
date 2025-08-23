# DSA Problem 81

'''
Problem Statement:
A palindrome is a number that reads the same backward as forward. Given a positive integer `n`, the task is to find the smallest palindrome greater than or equal to `n`. Your function should return this palindrome number.

Constraints:
- 1 <= n <= 10^4

Example:
Input: n = 123
Output: 131
Explanation: The smallest palindrome greater than 123 is 131.
'''

Solution:
def smallest_palindrome(n):
    """
    Returns the smallest palindrome greater than or equal to n.
    """
    while True:
        if str(n) == str(n)[::-1]:
            return n
        n += 1

# Check function to verify the correctness of the solution
def check_solution():
    assert smallest_palindrome(123) == 131, "Test case 1 failed"
    assert smallest_palindrome(678) == 686, "Test case 2 failed"
    assert smallest_palindrome(1) == 1, "Test case 3 failed"
    assert smallest_palindrome(999) == 1001, "Test case 4 failed"
    print("All test cases passed!")

check_solution()