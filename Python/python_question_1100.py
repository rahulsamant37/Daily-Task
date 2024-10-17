# Python Question: Find the Largest Rectangular Area in a Histogram
'''
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is shown in the shaded area, which has area = 5 * 2 = 10.

Input: heights = [2,4]
Output: 4
'''

# Solution
def largest_rectangle_area(heights):
    """
    Calculates the largest rectangular area in a histogram represented by the heights array.

    The approach uses a stack to keep track of the indices of increasing heights.
    When a height is encountered that is smaller than the height at the top of the stack,
    we pop the stack and calculate the area of the rectangle with the popped height as the
    minimum height and the distance between the current index and the index before the popped
    element in the stack as the width.
    """
    stack = []  # Stack to store indices of increasing heights
    max_area = 0
    n = len(heights)

    for i in range(n):
        # While the current height is smaller than the height at the top of the stack
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()  # Pop the top index from the stack
            # Calculate the area of the rectangle with height heights[top]
            # and width (i - stack[-1] - 1) if the stack is not empty,
            # or width i if the stack is empty.
            area = heights[top] * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, area)  # Update the maximum area
        stack.append(i)  # Push the current index onto the stack

    # Process the remaining elements in the stack
    while stack:
        top = stack.pop()  # Pop the top index from the stack
        # Calculate the area of the rectangle with height heights[top]
        # and width (n - stack[-1] - 1) if the stack is not empty,
        # or width n if the stack is empty.
        area = heights[top] * (n - stack[-1] - 1 if stack else n)
        max_area = max(max_area, area)  # Update the maximum area

    return max_area  # Return the maximum area

# Test cases
def test_largest_rectangle_area():
    assert largest_rectangle_area([2,1,5,6,2,3]) == 10
    assert largest_rectangle_area([2,4]) == 4
    assert largest_rectangle_area([4,2]) == 4
    assert largest_rectangle_area([0,0,0]) == 0
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([1,1]) == 2
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largest_rectangle_area([5,4,1,2]) == 8
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_rectangle_area()