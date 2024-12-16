# DSA Problem generated on 2024-12-17

Problem Statement:

Given a string of parentheses, write a function to find the longest balanced substring. A balanced substring is a string that contains an equal number of opening and closing parentheses.

Example:

Input: "(())()()"
Output: "(())()()"

Input: "(()(()))(()"
Output: "(()(()))"

Solution Code:

```
def longestBalancedSubstring(s):
    stack = []
    max_len = 0
    max_str = ""
    temp_str = ""
    temp_len = 0
    
    for char in s:
        if char == '(':
            stack.append(char)
            temp_str += char
            temp_len += 1
        elif char == ')':
            if stack:
                stack.pop()
                temp_str += char
                temp_len += 1
                if not stack:
                    if temp_len > max_len:
                        max_len = temp_len
                        max_str = temp_str
                        temp_str = ""
                        temp_len = 0
            else:
                if temp_len > max_len:
                    max_len = temp_len
                    max_str = temp_str
                temp_str = ""
                temp_len = 0
                
    if temp_len > max_len:
        max_len = temp_len
        max_str = temp_str
    return max_str
```

Time Complexity Analysis:

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate over the input string only once.

The space complexity is also O(n), as in the worst case, we might have to store the entire input string in the `temp_str` variable.

Note: This solution assumes that the input string only contains parentheses. If the input string can contain other characters, we would need to modify the solution accordingly.