# Python Question: Given a string, find the maximum count of consecutive vowels
'''
Problem: Given a string, find the maximum count of consecutive vowels. A vowel can be an 'a', 'e', 'i', 'o', or 'u'.

Example:
Input: s = "AaAbBcCdDeEfFgGhH"
Output: count = 4
Explanation: The maximum count of consecutive vowels is 4.

Input: s = "Hello, World!"
Output: count = 2
Explanation: The maximum count of consecutive vowels is 2.
'''

# Solution:
def solution(s):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    max_count = 0
    for char in s:
        if char in vowels:
            vowels[char] += 1
            if vowels[char] > max_count:
                max_count = vowels[char]
        else:
            vowels[char] = 1
    return max_count

def test_solution():
    assert solution("AaAbBcCdDeEfFgGhH") == 4, "Test Failed for input AaAbBcCdDeEfFgGhH"
    assert solution("Hello, World!") == 2, "Test Failed for input Hello, World!"

if __name__ == "__main__":
    test_solution()

# Output:
# Maximum count of consecutive vowels is 4
# Maximum count of consecutive vowels is 2