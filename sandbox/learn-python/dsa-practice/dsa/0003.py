# DSA Problem 3

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward, e.g., "radar". Given a string `s`, you are to find the length of the longest palindromic substring in `s`. Additionally, if there are multiple palindromic substrings of the same maximum length, return the lexicographically smallest one among them.

For example:
- If `s = "babad"`, the longest palindromic substrings are "bab" and "aba", both of length 3. Since "aba" is lexicographically smaller, the solution should return "aba".
- If `s = "cbbd"`, the longest palindromic substring is "bb", so the solution should return "bb".
'''

Solution:
```python
def longest_palindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest_palindrome = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        # Even length palindromes
        even_palindrome = expand_around_center(s, i, i + 1)
        
        # Determine if we found a new maximum
        max_palindrome = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome
        if len(max_palindrome) > len(longest_palindrome):
            longest_palindrome = max_palindrome
        elif len(max_palindrome) == len(longest_palindrome) and max_palindrome < longest_palindrome:
            longest_palindrome = max_palindrome
    
    return longest_palindrome

# Example usage
print(longest_palindrome("babad"))  # Output: "aba"
print(longest_palindrome("cbbd"))   # Output: "bb"
```

This solution expands around each character (considering both odd and even length palindromes) to find the longest palindromic substring. In case of a tie in length, the lexicographically smallest palindrome is chosen.