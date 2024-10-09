# DSA Problem generated on 2024-10-10

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parentheses substring. A valid parentheses substring is one where every open parenthesis has a corresponding close parenthesis.

**Example:**

Input: "(()())()"
Output: "(()())"

Input: ")()())"
Output: "()()"

**Solution Code:**
```
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    max_str = ""
    curr_len = 0
    curr_str = ""

    for c in s:
        if c == "(":
            stack.append("(")
            curr_str += c
            curr_len += 1
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                curr_str += c
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
                    max_str = curr_str
            else:
                stack = []
                curr_str = ""
                curr_len = 0

    return max_str
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the input string only once, and our operations inside the loop (pushing and popping from the stack, updating the current string and length) take constant time.

The space complexity is O(n) as well, since in the worst case, we might need to store all characters of the input string in the stack.

Note that this solution uses a stack to keep track of the open parentheses, and uses two variables (curr_len and curr_str) to keep track of the current valid parentheses substring. When we encounter a close parenthesis, we check if the stack is not empty and the top of the stack is an open parenthesis. If so, we pop the open parenthesis from the stack and update the current substring. If not, we reset the stack and the current substring. Finally, we return the longest valid parentheses substring found.