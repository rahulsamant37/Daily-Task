# DSA Problem generated on 2024-12-30

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` of parentheses, write a function `validate_parentheses` to validate whether the parentheses in the string are balanced and properly nested. The function should return `True` if the parentheses are valid, and `False` otherwise.

**Example:**

* Input: `s = "((()))"`
* Output: `True`
* Input: `s = "(()"
* Output: `False`

**Solution Code:**
```python
def validate_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
```
**Time Complexity Analysis:**

The time complexity of the `validate_parentheses` function is O(n), where n is the length of the input string `s`. This is because we iterate through the string once, and each operation (pushing or popping from the stack) takes constant time.

The space complexity is O(n) as well, since in the worst case, we might need to push all characters into the stack.

**Explanation:**

We use a stack to keep track of the opening parentheses. Whenever we encounter an opening parenthesis, we push it onto the stack. Whenever we encounter a closing parenthesis, we check if the stack is empty. If it is, it means there's no matching opening parenthesis, so we return `False`. If the stack is not empty, we pop the opening parenthesis from the stack.

At the end of the function, if the stack is empty, it means all parentheses were properly matched, so we return `True`. If the stack is not empty, it means there were unmatched opening parentheses, so we return `False`.