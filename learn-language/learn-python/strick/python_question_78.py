# Python Question: Count the number of vowels in a given string
'''
Input string may contain upper and lower case letters, and it may or may not contain spaces. Vowels are 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.

For example:
Input: "Python Programming"
Output: 9 (9 vowels: P, y, P, y, P, y, P, y, P)
Input: "HELLO WORLD"
Output: 5 (5 vowels: H, E, L, L, W)
'''

def count_vowels(input_str):
    # Create a dictionary to store count of vowels
    vowel_count = {}
    
    # Loop through each character in the input string
    for char in input_str:
        # Check if the character is a vowel
        if char in 'aeiouAEIOU':
            # If the character is a vowel, increment its count in the dictionary
            if char not in vowel_count:
                vowel_count[char] = 1
            else:
                vowel_count[char] += 1
    
    # Return a dictionary containing the count of vowels
    return vowel_count

# Test the function with some example inputs
input_str1 = "Python Programming"
print(count_vowels(input_str1))  # Output: {'P': 1, 'y': 2, 'P': 1, 'y': 1, 'P': 1, 'y': 1, 'W': 1, 'O': 1, 'r': 1, 'g': 1, 'M': 1, 'n': 1, 'G': 1, 'e': 1, 'l': 1, 'l': 1, 'l': 1, 'l': 1, 'o': 1, 'n': 1, 'g': 1, 'g': 1, 'a': 1, 'e': 1, 'n': 1, 'i': 1, 'n': 1, 'e': 1, 'n': 1, 'r': 1, 'u': 1}

input_str2 = "Hello World"
print(count_vowels(input_str2))  # Output: {'H': 1, 'E': 1, 'L': 1, 'l': 4, 'o': 1, 'W': 1, 'r': 1, 'd': 1}