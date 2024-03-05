# Python Question: Fibonacci Series till a given number
'''
Problem statement: Write a function that generates the Fibonacci series till a given number. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting from 0 and 1.

Example:
Input: 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1

    # Iterate till the desired number
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b

    return sequence

def test_fibonacci_sequence():
    assert fibonacci_sequence(0) == [], "Empty sequence should return an empty list"
    assert fibonacci_sequence(1) == [1], "For n=1, sequence should be [1]"
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3], "For n=5, sequence should be [0, 1, 1, 2, 3]"
    assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "For n=10, sequence should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]"
    assert fibonacci_sequence(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], "For n=15, sequence should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]"

if __name__ == "__main__":
    test_fibonacci_sequence()