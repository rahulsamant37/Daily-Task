# Python Question: Finding the largest number in a list of numbers

# Problem Statement
'''
Given a list of integers, find the largest number in the list.

Example:
Input: [5, 10, 20, 30, 40]
Output: 40
'''

# Solution
def largest_number(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # Return the first element (largest number) from the sorted list
    return numbers[0]

# Test cases
def test_largest_number():
    # Test with a list of integers
    assert largest_number([5, 10, 20, 30, 40]) == 40, "Expected: 40, Actual: " + str(largest_number([5, 10, 20, 30, 40]))

    # Test with an empty list
    assert largest_number([]) == 0, "Expected: 0, Actual: " + str(largest_number([]))

    # Test with a list containing only one number
    assert largest_number([100]) == 100, "Expected: 100, Actual: " + str(largest_number([100]))

    # Test with a list containing repeated numbers
    assert largest_number([1, 2, 3, 3, 4, 4, 5]) == 5, "Expected: 5, Actual: " + str(largest_number([1, 2, 3, 3, 4, 4, 5]))

# Main Program
if __name__ == "__main__":
    test_largest_number()