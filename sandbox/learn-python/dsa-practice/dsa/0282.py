# DSA Problem 282

'''
Problem Statement:
A "lucky" number is defined as a positive integer that contains only the digits 4 and 7. For example, 47 and 774 are lucky numbers. Given a positive integer n, write a function that returns the count of lucky numbers that are less than or equal to n.

For instance, for n = 100, the lucky numbers are 4, 7, 44, 47, 74, 77, making a total of 6 lucky numbers.
'''

Solution:
```python
def count_lucky_numbers(n):
    def generate_lucky_numbers(limit):
        lucky_numbers = []
        queue = ['4', '7']
        while queue:
            current = queue.pop(0)
            if int(current) <= limit:
                lucky_numbers.append(int(current))
                queue.append(current + '4')
                queue.append(current + '7')
        return lucky_numbers

    return len(generate_lucky_numbers(n))

# Test the function
print(count_lucky_numbers(100))  # Expected output: 6
print(count_lucky_numbers(80))  # Expected output: 4
```

In this solution, `count_lucky_numbers` generates all lucky numbers up to `n` using a queue-based approach to ensure that numbers are generated in increasing order. Once a lucky number exceeds `n`, it stops generating, making the solution efficient for large values of `n`.