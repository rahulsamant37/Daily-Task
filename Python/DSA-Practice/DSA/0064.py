# DSA Problem 64

'''
Problem Statement:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. Given a list of strings, write a function `count_palindromes` that returns the count of unique palindromic strings in the list. Note that the comparison should be case-insensitive, meaning 'Madam' and 'madam' are considered the same word.

Example:
For the input list `["Madam", "Racecar", "Anna", "Civic", "Madam"]`, the function should return `3` as there are three unique palindromic strings when case is ignored.

Constraints:
- The length of the list will not exceed 10^3.
- Each string in the list will have a length between 1 and 100.
'''

Solution:
```python
def count_palindromes(words):
    # Convert all words to lower case to ensure case-insensitive comparison
    words = [word.lower() for word in words]
    unique_palindromes = set()
    
    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            unique_palindromes.add(word)
    
    return len(unique_palindromes)

# Check function with provided data points
print(count_palindromes(["Madam", "Racecar", "Anna", "Civic", "Madam"]))  # Expected output: 3
```

This Python solution takes into account the case-insensitivity by converting all words to lowercase before checking if they are palindromes and adding them to a set to ensure uniqueness. The function finally returns the count of unique palindromic strings found in the list.