# Python Question: Fibonacci Series till N Elements
'''
Given a positive number n, print the first n numbers of the Fibonacci series.

Example:
Input: n = 5
Output: 144, 84, 55, 34, 21
'''

# Solution
def solution(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

def test_solution():
    n = 10
    solution(n)

if __name__ == "__main__":
    test_solution()