# Python Question: Implement a function to reverse a string
'''
You are required to implement a function that takes a string as input and returns a new string with the characters reversed. For example, if the input is "Python", the output should be "hyotP".
'''

# Solution
def reverse_string(s: str) -> str:
    return s[::-1]

# Test cases
def test_reverse_string():
    assert reverse_string("") == ""  # Empty string
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("Python") == "hyotP"

if __name__ == "__main__":
    test_reverse_string()