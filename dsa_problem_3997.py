# DSA Problem generated on 2024-09-24

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string `s` containing parentheses, write a function to find the longest valid parentheses substring. A valid parentheses substring is a sequence of characters where every open parenthesis has a corresponding close parenthesis and vice versa.

**Example:**

Input: `s = "(()())()(())"`
Output: `"(()())"` because it is the longest valid parentheses substring.

**Solution Code:**
```
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    max_substr = ""
    curr_len = 0
    curr_substr = ""

    for char in s:
        if char == "(":
            stack.append(char)
            curr_substr += char
            curr_len += 1
        elif char == ")" and stack:
            stack.pop()
            curr_substr += char
            curr_len += 1
            if not stack:
                if curr_len > max_len:
                    max_len = curr_len
                    max_substr = curr_substr
                curr_len = 0
                curr_substr = ""
        else:
            curr_len = 0
            curr_substr = ""

    return max_substr
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. This is because we only iterate through the input string once, and the operations inside the loop take constant time.

The space complexity is O(n) as well, because in the worst case, we might need to store all characters in the stack and the `curr_substr` variable.

**Explanation:**

The solution uses a stack to keep track of the open parentheses. When we encounter a close parenthesis, we check if the stack is not empty. If it's not empty, it means we have a matching open parenthesis, and we pop it from the stack. We also update the current substring and its length.

If the stack is empty when we encounter a close parenthesis, it means we have a mismatch, and we reset the current substring and its length.

We keep track of the maximum length and the corresponding substring as we iterate through the input string. Finally, we return the longest valid parentheses substring.

Note that this solution assumes that the input string only contains parentheses characters. If the input string can contain other characters, additional checks would be needed to handle them correctly.