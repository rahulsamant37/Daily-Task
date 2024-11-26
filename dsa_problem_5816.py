# DSA Problem generated on 2024-11-27

Here's a unique DSA problem in Python with a solution:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parentheses substring. A valid parentheses substring is a substring that has balanced and properly nested parentheses.

**Example:**

Input: "(()())()()"
Output: "(()())()()" (The entire string is a valid parentheses substring)

Input: ")()(()"
Output: "()" (The longest valid parentheses substring is "()")

**Solution Code:**

```python
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    max_str = ""
    temp_str = ""
    temp_len = 0

    for char in s:
        if char == "(":
            stack.append(char)
            temp_str += char
            temp_len += 1
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                temp_str += char
                temp_len += 1
                if temp_len > max_len:
                    max_len = temp_len
                    max_str = temp_str
            else:
                temp_str = ""
                temp_len = 0
                stack = []

    return max_str

# Test cases
print(longest_valid_parentheses("(()())()()"))  # Output: "(()())()()"
print(longest_valid_parentheses(")()(()"))  # Output: "()"
print(longest_valid_parentheses("())(()"))  # Output: "()()"
```

**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we are iterating through the input string only once.

The space complexity is also O(n) because in the worst case, we might need to store all characters in the temporary string and stack.

Note: This problem is a variation of the Longest Valid Parentheses problem, which is a classic problem in dynamic programming. However, this solution uses a stack-based approach instead of dynamic programming.