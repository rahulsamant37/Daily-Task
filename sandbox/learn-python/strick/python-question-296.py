# Python Question: Find the Largest Rectangular Area in a Histogram
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example, given heights = [2,1,5,6,2,3],
return 10.

Explanation:
The largest rectangle is shown in the shaded area, which has area = 5 * 2 = 10.

Input: [2,1,5,6,2,3]
Output: 10

Input: [6, 2, 5, 4, 5, 1, 6]
Output: 12

Input: [4, 2, 0, 3, 2, 5]
Output: 6
'''

# Solution
def solution():
    def largestRectangleArea(heights):
        """
        Calculates the largest rectangular area in a histogram.

        Args:
            heights: A list of non-negative integers representing the histogram bar heights.

        Returns:
            The area of the largest rectangle in the histogram.
        """
        stack = []  # Store indices of bars in increasing order of height
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Treat the end of the array as height 0
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

    return largestRectangleArea


# Test cases
def test_solution():
    assert solution()([2,1,5,6,2,3]) == 10, "Test Case 1 Failed"
    assert solution()([6, 2, 5, 4, 5, 1, 6]) == 12, "Test Case 2 Failed"
    assert solution()([4, 2, 0, 3, 2, 5]) == 6, "Test Case 3 Failed"
    assert solution()([2, 1, 2]) == 3, "Test Case 4 Failed"
    assert solution()([1]) == 1, "Test Case 5 Failed"
    assert solution()([0]) == 0, "Test Case 6 Failed"
    assert solution()([5,4,3,2,1]) == 9, "Test Case 7 Failed"
    assert solution()([1,2,3,4,5]) == 9, "Test Case 8 Failed"
    assert solution()([]) == 0, "Test Case 9 Failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()