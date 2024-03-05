# Python Question: Fibonacci Series till Number N
'''
Problem Statement:
Given a positive integer 'n', print the Fibonacci series up to 'n'.

Example:
Input: n = 10
Output:
1 1 2 3 5 8 13 21 34 55 89
'''

# Solution
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

def test_fibonacci():
    print("Fibonacci Series till Number 10:")
    generate_fibonacci(10)

if __name__ == "__main__":
    test_fibonacci()