# DSA Problem 325

'''
Problem Statement:
A palindrome is a string that reads the same forwards and backwards, such as "madam" or "racecar". Given a string s, you are allowed to perform exactly one move on the string where you can choose two indices i and j (0 <= i, j < len(s)) and swap the characters at these positions. Determine if it's possible to make the string s a palindrome after exactly one move. Return `True` if it's possible, otherwise return `False`.

Example 1:
Input: s = "abccba"
Output: True
Explanation: The string is already a palindrome. No need to perform a swap.

Example 2:
Input: s = "abcdba"
Output: True
Explanation: Swapping the last 'a' and 'b' to make the string "abdcba" which is a palindrome.

Example 3:
Input: s = "abc"
Output: False
Explanation: It's not possible to make this string a palindrome with one swap.
'''

Solution:
```python
def can_be_palindrome_with_one_swap(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return True
    
    # Create a dictionary to count occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Count characters that appear an odd number of times
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # If more than two characters have an odd count, it's not possible to make it a palindrome with one swap
    if odd_count > 2:
        return False
    
    # Check pairs of characters from the start and end moving towards the center
    for i in range(len(s) // 2):
        if s[i] != s[~i]:  # ~i is equivalent to -(i+1)
            # Try swapping the mismatched characters with all other characters to see if we can form a palindrome
            for j in range(i + 1, len(s)):
                # Swap characters at positions i and j
                s_list = list(s)
                s_list[i], s_list[j] = s_list[j], s_list[i]
                # Check if the swapped string is a palindrome
                if s_list == s_list[::-1]:
                    return True
                # Swap back for the next iteration
                s_list[i], s_list[j] = s_list[j], s_list[i]
            return False
    return False

# Test cases
print(can_be_palindrome_with_one_swap("abccba"))  # True
print(can_be_palindrome_with_one_swap("abcdba"))  # True
print(can_be_palindrome_with_one_swap("abc"))     # False
```

This Python solution checks if a string can be transformed into a palindrome with exactly one swap. It first checks if the string is already a palindrome or if it can become one with a single swap, considering the character counts and attempting swaps where necessary.