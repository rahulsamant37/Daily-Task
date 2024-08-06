# Python Question: Find the Largest Rectangular Area in a Histogram
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is formed by bars of height 5 and 6, giving area = 5 * 2 = 10.
'''

# Solution
def largest_rectangle_area(heights):
    """
    Calculates the largest rectangular area in a histogram represented by a list of heights.

    Args:
        heights: A list of non-negative integers representing the heights of the histogram bars.

    Returns:
        The area of the largest rectangle in the histogram.
    """
    stack = []  # Stack to store the indices of the bars
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # Iterate through the heights, including a sentinel value at the end (0)
        # This ensures that all bars in the stack are processed at the end.
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            # If the current bar is shorter than the bar at the top of the stack,
            # or if we've reached the end of the histogram, we need to calculate
            # the area of the rectangle formed by the bar at the top of the stack.

            height = heights[stack.pop()]  # Pop the index of the bar from the stack
            width = i if not stack else i - stack[-1] - 1  # Calculate the width of the rectangle

            # If the stack is empty, the width is the current index (i)
            # Otherwise, the width is the distance between the current index (i) and the index
            # of the previous bar in the stack (stack[-1]), minus 1.

            max_area = max(max_area, height * width)  # Update the maximum area
        stack.append(i)  # Push the current index onto the stack

    return max_area

# Test cases
def test_largest_rectangle_area():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([4, 2]) == 4
    assert largest_rectangle_area([0]) == 0
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([2, 1, 2]) == 3
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largest_rectangle_area([5, 4, 3, 2, 1]) == 9
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9
    assert largest_rectangle_area([]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_rectangle_area()