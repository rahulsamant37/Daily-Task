# Python Question: Largest Rectangle in Histogram
'''
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Input: heights = [2,4]
Output: 4
'''

# Solution
def largestRectangleArea(heights):
    """
    Finds the largest rectangular area possible in a given histogram.

    Args:
        heights: A list of integers representing the heights of the histogram bars.

    Returns:
        The area of the largest rectangle in the histogram.
    """
    stack = []  # Stack to store indices of bars
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # Iterate through the heights, including a dummy height of 0 at the end
        # to ensure all bars in the stack are processed.
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            # While the stack is not empty and the current height is less than or equal
            # to the height of the bar at the top of the stack, calculate the area
            # of the rectangle formed by the bar at the top of the stack.
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i  # Calculate the width based on the stack
            max_area = max(max_area, height * width)

        stack.append(i)  # Push the current index onto the stack

    return max_area


# Test cases
def test_largestRectangleArea():
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2, 4]) == 4
    assert largestRectangleArea([4, 2, 0, 3, 2, 5]) == 6
    assert largestRectangleArea([0]) == 0
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([2, 1, 2]) == 3
    assert largestRectangleArea([5, 4, 1, 2]) == 8
    assert largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    print("All test cases passed!")


if __name__ == "__main__":
    test_largestRectangleArea()