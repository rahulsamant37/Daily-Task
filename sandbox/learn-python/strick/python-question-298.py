# Python Question: Valid Parentheses String Path

'''
Given a matrix of parentheses, determine if there exists a valid path from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1).
A valid path consists of only '(' and ')' characters, and at any point in the path, the number of open parentheses must be greater than or equal to the number of closed parentheses. The final path (at m-1, n-1) must have an equal number of open and closed parentheses.
You can only move down or right.

Input:
matrix = [["(", "(", ")"],
          [")", "(", ")"],
          ["(", "(", ")"]]

Output: True

Explanation:
One valid path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2). The string is "(()())" which is a valid parentheses string.

Input:
matrix = [["(", ")"],
          [")", "("]]

Output: False

'''

# Solution
def solution():
    def has_valid_path(matrix):
        m = len(matrix)
        n = len(matrix[0])

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col, balance):
            # Base case: out of bounds
            if not is_valid(row, col):
                return False

            # Update balance based on the current parenthesis
            if matrix[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            # If balance becomes negative, the path is invalid
            if balance < 0:
                return False

            # Base case: reached the destination
            if row == m - 1 and col == n - 1:
                return balance == 0

            # Explore the paths down and right
            return dfs(row + 1, col, balance) or dfs(row, col + 1, balance)

        # Start the DFS from the top-left corner with an initial balance of 0
        return dfs(0, 0, 0)

    return has_valid_path
    # Test cases
def test_solution():
    has_valid_path = solution()
    matrix1 = [["(", "(", ")"],
               [")", "(", ")"],
               ["(", "(", ")"]]
    assert has_valid_path(matrix1) == True

    matrix2 = [["(", ")"],
               [")", "("]]
    assert has_valid_path(matrix2) == False

    matrix3 = [["("]]
    assert has_valid_path(matrix3) == False

    matrix4 = [["(" , ")"]]
    assert has_valid_path(matrix4) == True

    matrix5 = [["("], [")"]]
    assert has_valid_path(matrix5) == True

    matrix6 = [["(", "(", "("],
               [")", ")", ")"]]
    assert has_valid_path(matrix6) == False

    matrix7 = [["(", "(", ")", ")"],
               ["(", ")", "(", ")"],
               ["(", "(", ")", ")"],
               ["(", "(", ")", ")"]]
    assert has_valid_path(matrix7) == True

if __name__ == "__main__":
    test_solution()