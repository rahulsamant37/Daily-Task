# Python Question: Largest Rectangle in Histogram
'''
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

Example:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle is shown in the shaded area, which has area = 5 * 2 = 10.

Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
'''

# Solution
def largestRectangleArea(heights):
    """
    Calculates the largest rectangle area in a histogram represented by the heights array.

    The approach uses a stack to keep track of the indices of bars in increasing order.
    When a bar with a height less than the top of the stack is encountered, it means
    we have found the right boundary for the rectangle formed by the bar at the top of the stack.
    We then pop the stack and calculate the area of the rectangle using the current index
    as the right boundary and the index of the bar below the top of the stack as the left boundary.

    Args:
        heights: A list of integers representing the heights of the bars in the histogram.

    Returns:
        The area of the largest rectangle in the histogram.
    """
    stack = []  # Stack to store indices of bars in increasing order of height
    max_area = 0
    n = len(heights)

    for i in range(n):
        # While the current bar is shorter than the bar at the top of the stack
        while stack and heights[i] < heights[stack[-1]]:
            # Pop the top of the stack
            top = stack.pop()
            # Calculate the area of the rectangle formed by the popped bar
            # Width is the distance between the current index and the index of the bar below the top of the stack
            # Height is the height of the popped bar
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)

        # Push the current index onto the stack
        stack.append(i)

    # After processing all bars, pop the remaining bars from the stack
    while stack:
        top = stack.pop()
        width = n if not stack else n - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area


# Test cases
def test_largestRectangleArea():
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2, 4]) == 4
    assert largestRectangleArea([4, 2]) == 4
    assert largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    assert largestRectangleArea([0]) == 0
    assert largestRectangleArea([1, 1]) == 2
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([5, 4, 3, 2, 1]) == 9
    assert largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert largestRectangleArea([1, 2, 3, 4, 5, 3, 3, 2, 1]) == 16
    print("All test cases passed!")


if __name__ == "__main__":
    test_largestRectangleArea()