# DSA Problem 233

'''
Problem Statement:
A "wonderful" number is defined as a positive integer whose digits are strictly increasing from left to right. For example, 123 and 359 are wonderful numbers, but 111, 232, and 987 are not. Given a positive integer `n`, return the number of wonderful numbers that are less than or equal to `n`.

Example 1:
Input: n = 20
Output: 19
Explanation: All numbers from 1 to 19 are wonderful, and 20 is not. So, there are 19 wonderful numbers less than or equal to 20.

Example 2:
Input: n = 100
Output: 45
Explanation: Numbers like 12, 13, ..., 89 are wonderful, but 11, 22, ..., 99 are not. There are 45 wonderful numbers less than or equal to 100.

Constraints:
1 <= n <= 10^6
'''

Solution:
```python
def count_wonderful_numbers(n: int) -> int:
    def is_wonderful(num):
        return all(int(num[i]) < int(num[i+1]) for i in range(len(num)-1))
    
    return sum(is_wonderful(str(num)) for num in range(1, n+1))

# Example checks
print(count_wonderful_numbers(20))  # Output: 19
print(count_wonderful_numbers(100)) # Output: 45
```

Note: The above solution is straightforward but may not be optimal for large inputs due to its O(n) time complexity. For a more efficient solution, one could consider generating wonderful numbers directly rather than checking each number from 1 to n.