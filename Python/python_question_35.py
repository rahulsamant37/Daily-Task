# Python Question: Finding the largest number possible within a given range
'''
Given two integers, n and m, find the largest number possible within the range n <= x <= m and print it.

Example:
Input: n = 4, m = 9
Output: 9999 (largest number within the range 4 <= x <= 9)
'''

# Solution
def largest_number(n, m):
    result = ""
    while n <= m:
        result = str(n) + result
        n += 1
    return result[::-1]

# Test cases
def test_largest_number():
    assert largest_number(4, 9) == "9999", "Incorrect result for input (4, 9)"
    assert largest_number(5, 10) == "99999", "Incorrect result for input (5, 10)"
    assert largest_number(0, 10) == "101010", "Incorrect result for input (0, 10)"

if __name__ == "__main__":
    test_largest_number()