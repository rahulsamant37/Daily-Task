# Python Question: Finding the largest number from three given numbers without using branching
'''
Problem statement: Given three numbers, find the largest number among them without using branching (if-else).
'''

# Solution
def find_largest_number(num1, num2, num3):
    # Create a new list with all the numbers in it
    numbers_list = [num1, num2, num3]

    # Sort the list in descending order
    numbers_list.sort(reverse=True)

    # Return the first element of the sorted list, as it is the largest number
    return numbers_list[0]

# Test cases
def test_solution():
    assert find_largest_number(5, 10, 3) == 10, "Expected: 10, Actual: " + str(find_largest_number(5, 10, 3))
    assert find_largest_number(9, 5, 8) == 9, "Expected: 9, Actual: " + str(find_largest_number(9, 5, 8))
    assert find_largest_number(1, 6, 9) == 9, "Expected: 9, Actual: " + str(find_largest_number(1, 6, 9))

if __name__ == "__main__":
    test_solution()