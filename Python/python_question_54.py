# Python Question: Given a string, find the length of the longest substring without repeating characters

'''
For example, consider the string 'aaabb'. The longest substring without repeating characters in this string is 'aaab', which has a length of 5.
'''

# Solution
def find_longest_substring(s):
    # Initialize variables
    max_len = 0
    start = 0
    char_set = set()

    # Iterate over the string
    for i, char in enumerate(s):
        # Check if the current character is already present in the set
        if char in char_set:
            # Update the start index and length if necessary
            if len(s[start:i]) > max_len:
                max_len = len(s[start:i])
                start = i

        # Add the current character to the set
        char_set.add(char)

    return max_len

# Test cases
string1 = 'aaabb'
print("Longest substring without repeating characters in", string1, "is", find_longest_substring(string1))

string2 = 'level'
print("Longest substring without repeating characters in", string2, "is", find_longest_substring(string2))

string3 = 'python'
print("Longest substring without repeating characters in", string3, "is", find_longest_substring(string3))