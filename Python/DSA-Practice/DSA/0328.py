# DSA Problem 328

'''
Problem Statement:
A positive integer is considered "lucky" if it contains either the digit 4 or 7, and the total number of digits 4 and 7 in the number is exactly 3. For example, 477, 444, and 774 are lucky numbers, but 44, 4777, and 764 are not. You are given a positive integer N. Your task is to find the next lucky number greater than N. If no such number exists within the first 1000 numbers greater than N, return -1.

Note: Since the number can be very large, you should handle it as a string.
'''

Solution:
```python
def is_lucky(num):
    count = num.count('4') + num.count('7')
    return count == 3

def next_lucky(N):
    for i in range(N + 1, N + 1001):
        if is_lucky(str(i)):
            return i
    return -1

# Example usage
N = 744
print(next_lucky(N))  # Output should be 774
```

Explanation:
The function `is_lucky` checks if the number contains exactly three digits that are either 4 or 7. The function `next_lucky` iterates over the next 1000 numbers after N and uses `is_lucky` to check if any of these numbers are lucky. If a lucky number is found, it is returned; otherwise, the function returns -1.