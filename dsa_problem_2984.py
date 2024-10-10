# DSA Problem generated on 2024-10-11

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parentheses substring. A valid parentheses substring is a substring that has balanced parentheses, i.e., every opening parenthesis has a corresponding closing parenthesis.

**Example:**

Input: `"(()())()"`
Output: `"(()())"`

Input: `")()())("`
Output: `"()()"`

**Solution Code:**
```python
def longest_valid_parentheses(s: str) -> str:
    stack = []
    max_len = 0
    max_substr = ""
    curr_len = 0
    curr_substr = ""

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
                if not stack:
                    curr_len = i + 1
                    curr_substr = s[i - curr_len + 1:i + 1]
                else:
                    curr_len = i - stack[-1]
                    curr_substr = s[stack[-1] + 1:i + 1]
                if curr_len > max_len:
                    max_len = curr_len
                    max_substr = curr_substr
            else:
                curr_len = 0
                curr_substr = ""

    return max_substr
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string only once, using a single loop.

The space complexity is O(n) as well, because in the worst case, we might need to store all the indices of the opening parentheses in the stack.

Here's a breakdown of the time complexity:

* The loop iterates n times, where n is the length of the input string.
* Inside the loop, we perform constant-time operations (pushing/popping from the stack, updating variables) except for one case: when we find a closing parenthesis and the stack is not empty. In this case, we update the `curr_len` and `curr_substr` variables, which takes O(k) time, where k is the length of the current valid parentheses substring. However, since k is bounded by n, we can consider this operation as O(n) in the worst case.
* Therefore, the total time complexity is O(n).

Note that this solution has a linear time complexity because we use a stack to keep track of the opening parentheses, which allows us to find the longest valid parentheses substring in a single pass.