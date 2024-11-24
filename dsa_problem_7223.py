# DSA Problem generated on 2024-11-25

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string of parentheses, write a function to find the longest valid parentheses sequence. A valid parentheses sequence is a sequence of parentheses that can be matched correctly. For example, "(())()" is a valid parentheses sequence, but "()(" is not.

**Problem Example:**

Input: "(()())()"
Output: 6 (The longest valid parentheses sequence is "(()())" which has a length of 6)

Input: "()("
Output: 2 (The longest valid parentheses sequence is "()()" which has a length of 2)

**Solution Code:**
```
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    curr_len = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
                if not stack:
                    curr_len = i + 1
                else:
                    curr_len = i - stack[-1]
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0
    return max_len
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we only iterate through the input string once, and each operation within the loop takes constant time.

Here's a breakdown of the time complexity:

* The outer loop iterates n times, so it has a time complexity of O(n).
* The inner operations (pushing and popping from the stack, and updating `curr_len` and `max_len`) take constant time, so they don't affect the overall time complexity.

The space complexity is O(n) as well, since in the worst case, the stack can grow up to a size of n.

**Explanation:**

The solution uses a stack to keep track of the indices of the opening parentheses. When we encounter a closing parenthesis, we check if the stack is empty. If it's not empty, we pop the top element from the stack, which represents the index of the matching opening parenthesis. We then calculate the length of the current valid parentheses sequence by subtracting the index of the opening parenthesis from the current index. If the stack is empty, we reset the current length to 0. We keep track of the maximum length of the valid parentheses sequence and return it at the end.

This solution has a linear time complexity and uses a stack to efficiently keep track of the matching parentheses.