# Python Question: Largest Rectangle in Histogram
'''
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the shaded area, which has area = 10 unit.

Input: heights = [2,4]
Output: 4
'''

# Solution
def largestRectangleArea(heights):
    """
    Calculates the area of the largest rectangle in a histogram.

    Args:
        heights: A list of integers representing the height of each bar in the histogram.

    Returns:
        The area of the largest rectangle in the histogram.
    """
    stack = []  # Stack to store indices of bars.  The stack maintains increasing order of heights.
    max_area = 0
    n = len(heights)

    for i in range(n + 1):  # Iterate through the heights, including a sentinel value at the end
        # The sentinel value (virtual bar of height 0) helps to clear the stack and process all remaining bars.
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            # If the current bar is shorter than the bar at the top of the stack,
            # or we've reached the end of the histogram (i == n),
            # calculate the area of the rectangle formed by the bar at the top of the stack.
            height = heights[stack.pop()]  # Height of the bar at the top of the stack
            width = i if not stack else i - stack[-1] - 1  # Width of the rectangle
            # If stack is empty, the width is i (from 0 to i).
            # Otherwise, the width is the distance between the current bar and the previous bar in the stack.
            max_area = max(max_area, height * width)  # Update the maximum area

        stack.append(i)  # Push the index of the current bar onto the stack

    return max_area

# Test cases
def test_largestRectangleArea():
    assert largestRectangleArea([2,1,5,6,2,3]) == 10
    assert largestRectangleArea([2,4]) == 4
    assert largestRectangleArea([4,2,0,3,2,4,3,4]) == 10
    assert largestRectangleArea([0,0,0,0,0]) == 0
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([1,1]) == 2
    assert largestRectangleArea([2,1,2]) == 3
    assert largestRectangleArea([6,2,5,4,5,1,6]) == 12
    assert largestRectangleArea([5,4,1,2]) == 8
    assert largestRectangleArea([3,6,5,7,4,8,1,0]) == 20
    print("All test cases passed!")

if __name__ == "__main__":
    test_largestRectangleArea()