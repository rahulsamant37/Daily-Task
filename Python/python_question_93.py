# Python Question: Count vowels in a string without using any built-in method
'''
The task is to count the number of vowels (a, e, i, o, u) present in a given string without using any built-in method.

Example:
Input: "Python programming language"
Output: 6 (There are 2 'p', 1 'y', 1 't', 1 'h', 1 'o', and 2 vowels)
'''

def solution():
    # Create an empty dictionary to store the count of vowels
    vowel_count = {}

    # Iterate through the characters in the input string
    for char in input_string:
        # Check if the character is a vowel or not
        if char in "aeiou":
            # Update count if the character is a vowel
            vowel_count[char] = vowel_count.get(char, 0) + 1
        else:
            # Reset the count if the character is not a vowel
            vowel_count[char] = 0

    # Return the dictionary containing the count of vowels
    return vowel_count


def test_solution():
    # Test the solution with various input strings
    print(solution("Python programming language"))  # Output: {'P': 1, 'y': 1, 'p': 1, 'r': 1, 'g': 1, 'n': 1, 'l': 1, 'a': 1, 'e': 1, 'h': 0, 'm': 0, 't': 0}
    print(solution("Hello, world!"))  # Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, ',': 1, '!': 1}
    print(solution("12345"))  # Output: {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1}

if __name__ == "__main__":
    test_solution()