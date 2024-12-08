# DSA Problem 280

'''
Problem Statement:
A group of students are participating in a book exchange event. Each student brings one book and receives one book in return. The event organizer decides to make the exchange more interesting by implementing a rule: no student should receive a book of the same genre they brought. Given a list of genres (as strings) that each of the N (1 ≤ N ≤ 100) students will bring, determine if it's possible to organize the book exchange to satisfy the rule. If possible, return "YES", otherwise return "NO". Assume each genre appears at least twice in the list, and the genres are represented by single lowercase English letters.

Example:
For genres = "aaabbb", the output should be "YES".
For genres = "aabbcc", the output should be "YES".
For genres = "aabb", the output should be "NO".

Constraints:
- 1 ≤ N ≤ 100
- Each genre appears at least twice.
- The list of genres is represented by a string of lowercase English letters.
'''

Solution:
def can_exchange_books(genres):
    """
    Determines if it's possible to organize a book exchange such that no student
    receives a book of the same genre they brought.
    """
    from collections import Counter
    
    genre_counts = Counter(genres)
    # If any genre appears an odd number of times, it's impossible to pair them up.
    for count in genre_counts.values():
        if count % 2 != 0:
            return "NO"
    return "YES"

# Test cases
print(can_exchange_books("aaabbb"))  # Expected output: "YES"
print(can_exchange_books("aabbcc"))  # Expected output: "YES"
print(can_exchange_books("aabb"))    # Expected output: "NO"
print(can_exchange_books("abcabc"))  # Expected output: "YES"
print(can_exchange_books("aabbc"))  # Expected output: "NO"

# Note: The function assumes the input meets the problem's constraints, i.e., each genre appears at least twice,
# and the length of the string is within the given range.
'''

This problem solution checks the feasibility of organizing a book exchange under the given constraints by leveraging the `Counter` class from the `collections` module to count occurrences of each genre. If any genre appears an odd number of times, it's impossible to pair up all students with different genres, hence the exchange cannot be organized as desired, returning "NO". Otherwise, "YES" is returned, indicating the exchange can proceed under the rule.