# Python Question: Calculate the sum of digits of a number until the number becomes 0

'''
Input a positive integer n. Find the sum of its digits until the number becomes 0.

Example:
Input: n = 123
Output: 6 (1 + 2 + 3 = 6)
Input: n = 456
Output: 10 (4 + 5 + 6 = 10)
'''

def solution(n):
    '''
    Function to calculate the sum of digits of a number until the number becomes 0
    '''
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def test_solution():
    assert solution(123) == 6, 'Expected: 6, Actual: {}'.format(solution(123))
    assert solution(456) == 10, 'Expected: 10, Actual: {}'.format(solution(456))
    assert solution(1234) == 10, 'Expected: 10, Actual: {}'.format(solution(1234))
    assert solution(12345) == 15, 'Expected: 15, Actual: {}'.format(solution(12345))
    assert solution(100) == 50, 'Expected: 50, Actual: {}'.format(solution(100))

if __name__ == "__main__":
    test_solution()