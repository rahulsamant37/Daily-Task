# DSA Problem 306

'''
Problem Statement:
You are given a list of integers representing the heights of various towers in a city skyline. Your task is to find the maximum area of the rectangle that can be formed by concatenating any number of consecutive towers. The width of each tower is considered to be 1 unit. For instance, if the heights are [2, 1, 5, 6, 2, 3], the maximum area rectangle formed by these towers is 10, which can be achieved by the towers with heights [5, 6].

Note:
- The list will contain at least one tower height.
- Each height is a positive integer.
'''

Solution:
```python
def max_rectangle_area(heights):
    """
    Calculates the maximum rectangular area formed by consecutive towers.
    """
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = (heights[top] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        area = (heights[top] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Check function to verify the solution with provided data points
def check_solution():
    assert max_rectangle_area([2,1,5,6,2,3]) == 10, "Test case 1 failed"
    assert max_rectangle_area([2,4]) == 4, "Test case 2 failed"
    assert max_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This code snippet provides a solution to the problem statement given above by using a stack to keep track of the tower indices and calculating areas by popping out indices under certain conditions to find the maximum possible rectangular area that can be formed.