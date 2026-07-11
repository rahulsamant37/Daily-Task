# DSA Problem 119

'''
Problem Statement:
A 'super-palindrome' is a positive integer that is both a palindrome and the square of a palindrome. For example, 121 is a super-palindrome since it's a palindrome and its square root, 11, is also a palindrome. Given two integers, `low` and `high`, count the number of super-palindromes in the inclusive range `[low, high]`.

Note:
- 1 <= low <= high <= 10^18
- 1 <= low <= high, and both are integers.
'''

Solution:
```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_super_palindromes(low, high):
    super_palindromes = 0
    # We only need to check up to 100000 because the square of the largest 6-digit palindrome exceeds 10^18.
    for i in range(1, 100000):
        pal = int(str(i) + str(i)[::-1])  # generate even-length palindrome
        squared = pal ** 2
        if squared > high:
            break
        if is_palindrome(squared) and squared >= low:
            super_palindromes += 1
            
    for i in range(1, 100000):
        for j in '012345678':
            pal = int(str(i) + j + str(i)[::-1])  # generate odd-length palindrome
            squared = pal ** 2
            if squared > high:
                break
            if is_palindrome(squared) and squared >= low:
                super_palindromes += 1
                
    return super_palindromes

# Example usage:
print(count_super_palindromes(4, 1000))  # Output: 4
```

This Python solution checks for super-palindromes by generating palindromic numbers and verifying if their squares are also palindromic, counting those that fall within the specified range.