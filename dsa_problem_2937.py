# DSA Problem generated on 2024-12-10

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string of parentheses, write a function to return the minimum number of removals required to make the string valid. A string of parentheses is considered valid if every open parenthesis has a corresponding close parenthesis and vice versa.

**Example:**

Input: "())(("
Output: 4 (Remove 2 closing and 2 opening parentheses to make the string valid)

**Solution Code:**
```python
def min_removals_to_make_valid(s):
    stack = []
    removals = 0

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                removals += 1

    removals += len(stack)
    return removals
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string. This is because we only iterate through the input string once, and each operation inside the loop takes constant time.

Here's a breakdown of the time complexity:

* Iterating through the input string: O(n)
* Pushing and popping from the stack: O(1) amortized, since we only push and pop elements from the stack a maximum of n times.
* Incrementing the removals counter: O(1)

Therefore, the overall time complexity is O(n).

**Explanation:**

The solution uses a stack to keep track of the opening parentheses. When we encounter a closing parenthesis, we check if the stack is not empty and the top element is an opening parenthesis. If it is, we pop the opening parenthesis from the stack, indicating that it has been matched with the closing parenthesis. If the stack is empty or the top element is not an opening parenthesis, we increment the removals counter, indicating that the closing parenthesis is unmatched.

At the end, we add the remaining elements in the stack to the removals counter, since they represent unmatched opening parentheses that need to be removed to make the string valid.