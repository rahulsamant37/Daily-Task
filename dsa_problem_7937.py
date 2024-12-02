# DSA Problem generated on 2024-12-03

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parenthetical substring. A valid parenthetical substring is a sequence of parentheses where every open parenthesis has a corresponding closing parenthesis and vice versa.

**Example:**

Input: `s = "(())()()"`
Output: `(())()()` (entire string is valid)

Input: `s = "()(()))"`
Output: `()(()` (longest valid substring)

Input: `s = "(()))()()"`
Output: `()()` (longest valid substring)

**Solution Code:**
```python
def longest_valid_parentheses(s: str) -> str:
    stack = []
    max_len = 0
    max_substring = ""
    temp_len = 0
    temp_substring = ""

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
                temp_len += 2
                temp_substring = s[i - temp_len + 1:i + 1]
                if temp_len > max_len:
                    max_len = temp_len
                    max_substring = temp_substring
            else:
                temp_len = 0
                temp_substring = ""

    return max_substring
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string only once, using a single pass to keep track of the stack and the longest valid substring.

The space complexity is O(n) as well, since in the worst case, the stack can grow up to the size of the input string.

**Explanation:**

The solution uses a stack to keep track of the open parentheses. When we encounter a closing parenthesis, we check if the stack is not empty. If it's not empty, we pop the top element (which represents the corresponding open parenthesis) and update the temporary length and substring. If the temporary length is greater than the maximum length found so far, we update the maximum length and substring.

When we encounter a closing parenthesis and the stack is empty, it means we've encountered an unmatched closing parenthesis, so we reset the temporary length and substring.

Finally, we return the longest valid substring found.

This solution has a linear time complexity and uses a moderate amount of extra space to store the stack and temporary substrings.