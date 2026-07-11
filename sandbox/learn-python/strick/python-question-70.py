# Python Question: Find the largest number in a list of given numbers
'''
Given a list of numbers, write a function that finds the largest number in the list.

Example:
Input: [5, 10, 3, 7, 20]
Output: 20 (The largest number in the list)
'''

# Solution
def find_largest_number(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)
    # Return the last element of the sorted list, which is the largest number
    return numbers[-1]

# Test cases
def test_find_largest_number():
    # Test list of numbers
    test_cases = [
        [1, 10, 100],
        [5, 10, 3, 7, 20],
        [1, 9, 50, -3, 100]
    ]
    
    for numbers in test_cases:
        result = find_largest_number(numbers)
        print(f"The largest number in the list {numbers} is {result}")

if __name__ == "__main__":
    test_find_largest_number()