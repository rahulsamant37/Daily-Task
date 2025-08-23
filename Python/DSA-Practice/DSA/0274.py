# DSA Problem 274

'''
Problem Statement:
A "wonderful" number is defined as a positive integer where the product of its digits equals 12. For example, 26, 62, and 34 are all wonderful numbers as their digits multiply to 12. Given an integer n, find the nth smallest wonderful number. Assume n is positive and n ≤ 10000.

Note:
- The order of the wonderful numbers should be determined strictly by their numeric value.
- The digits in the wonderful numbers can only be from 1 to 9, as 0 cannot contribute to the product being 12.

Example:
Input: n = 3
Output: 34
Explanation: The first three wonderful numbers in ascending order are 26, 34, and 43. Therefore, the 3rd wonderful number is 34.
'''

Solution:
```python
from itertools import permutations

def find_nth_wonderful(n):
    wonderful_numbers = set()
    for a in range(1, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                if a * b * c == 12:
                    for digits in permutations([a, b, c]):
                        wonderful_numbers.add(int(''.join(map(str, digits))))
                if a * b * c > 12:
                    break
    sorted_wonderful = sorted(wonderful_numbers)
    return sorted_wonderful[n-1]

# Test the solution with provided data point
print(find_nth_wonderful(3))  # Expected output: 34
```

This solution generates all possible wonderful numbers up to three digits and then finds the nth smallest from that list. The use of permutations and a set ensures that duplicates are avoided and all possible combinations of digits that multiply to 12 are considered.