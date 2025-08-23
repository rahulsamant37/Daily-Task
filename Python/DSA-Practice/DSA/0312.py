# DSA Problem 312

'''
Problem Statement:
A "wonderful" number is defined as an integer that is part of a sequence starting from 1 and increasing by a fixed positive integer 'step' until it reaches or exceeds a given positive integer 'limit'. For instance, if 'step' is 2 and 'limit' is 10, the sequence is 1, 3, 5, 7, 9, which makes each number in this sequence a "wonderful" number. Your task is to write a function `count_wonderful_numbers` that takes two arguments 'step' and 'limit' and returns the count of "wonderful" numbers in the sequence.

Example:
For step = 3 and limit = 20, the "wonderful" numbers are 1, 4, 7, 10, 13, 16, 19. Hence, the function should return 7.
'''

Solution:
```python
def count_wonderful_numbers(step, limit):
    """
    Counts the number of wonderful numbers given a step and a limit.
    
    Parameters:
    step (int): The step size to generate the sequence of wonderful numbers.
    limit (int): The upper limit of the sequence.
    
    Returns:
    int: The count of wonderful numbers in the sequence.
    """
    # Calculate the count of wonderful numbers
    return (limit - 1) // step + 1

# Function to check the correctness of the count_wonderful_numbers function
def check_function():
    assert count_wonderful_numbers(3, 20) == 7, "Test case 1 failed"
    assert count_wonderful_numbers(2, 10) == 5, "Test case 2 failed"
    assert count_wonderful_numbers(5, 25) == 5, "Test case 3 failed"
    assert count_wonderful_numbers(1, 100) == 100, "Test case 4 failed"
    print("All test cases passed!")

# Run the check function to verify the solution
check_function()
```

This solution includes a simple mathematical calculation to determine the count of "wonderful" numbers based on the given 'step' and 'limit'. The check function is used to validate the correctness of the solution with different inputs.