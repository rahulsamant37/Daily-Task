# Python Question: Count the number of vowels in a given string
'''
Problem Statement: Given a string, count the number of vowels present in it. Vowels are 'a', 'e', 'i', 'o', and 'u'.

Example:
Input: "Python is a popular programming language"
Output: 14 (1 a, 2 i, 2 o, and 9 y)
'''

# Solution
def count_vowels(input_string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    
    for char in input_string.lower():
        if char in vowels:
            count += 1
    return count

# Test Cases
def test_solution():
    test_cases = [
        ("Python is a popular programming language", 14),
        ("Let's learn Python", 10),
        ("Hello, World!", 4),
        ("Python is a turtle", 12)
    ]
    
    for test_case in test_cases:
        input_string, expected_count = test_case
        print(f"Input: {input_string}")
        if count_vowels(input_string) != expected_count:
            print("FAIL: Expected", expected_count, "but got", count_vowels(input_string))

if __name__ == "__main__":
    test_solution()