# Python Question: Largest Rectangle in Histogram
'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is shown in the shaded area, which has area = 5 * 2 = 10.

Input: heights = [2,4]
Output: 4
'''

# Solution
def largestRectangleArea(heights):
    """
    Calculates the largest rectangular area in a histogram represented by the heights array.

    The approach uses a stack to keep track of increasing bar indices. When a bar of smaller height
    is encountered, we pop the stack and calculate the area of the rectangle formed by the popped bar.
    The width of the rectangle is determined by the current index and the index of the previous smaller bar
    (which is now at the top of the stack).

    Args:
        heights: A list of integers representing the heights of the histogram bars.

    Returns:
        The maximum rectangular area in the histogram.
    """
    stack = []  # Store indices of increasing heights
    max_area = 0
    n = len(heights)

    for i in range(n):
        # While the current bar is shorter than the bar at the top of the stack,
        # pop the stack and calculate the area.
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        # Push the current index onto the stack.
        stack.append(i)

    # After processing all bars, pop the remaining bars from the stack and calculate their areas.
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Test cases
def test_largestRectangleArea():
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2, 4]) == 4
    assert largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largestRectangleArea([0]) == 0
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([1, 1]) == 2
    assert largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert largestRectangleArea([5, 4, 3, 2, 1]) == 9
    print("All test cases passed!")

if __name__ == "__main__":
    test_largestRectangleArea()