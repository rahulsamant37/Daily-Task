# DSA Problem generated on 2024-09-23

Here's a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parentheses substring. A valid parentheses substring is one that has a matching opening and closing parenthesis.

**Example:**

Input: `")()())()("`
Output: `"()()"`

**Solution Code:**
```python
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    max_substr = ""
    curr_len = 0
    curr_substr = ""

    for c in s:
        if c == "(":
            stack.append("(")
            curr_substr += "("
            curr_len += 1
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                curr_substr += ")"
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
                    max_substr = curr_substr
            else:
                stack = []
                curr_len = 0
                curr_substr = ""

    return max_substr
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the input string only once, and the operations within the loop take constant time.

The space complexity is O(n) as well, since we use a stack to keep track of the opening parentheses, and in the worst case, the stack will grow to the size of the input string.

**Explanation:**

The solution uses a stack to keep track of the opening parentheses. When we encounter a closing parenthesis, we check if the top of the stack has a matching opening parenthesis. If it does, we pop the opening parenthesis from the stack and add the closing parenthesis to the current substring. If the current substring is longer than the maximum substring found so far, we update the maximum substring.

If we encounter a closing parenthesis without a matching opening parenthesis, we reset the stack, current substring, and current length.

Finally, we return the longest valid parentheses substring found.

This solution has a linear time complexity and a linear space complexity, making it efficient for large input strings.