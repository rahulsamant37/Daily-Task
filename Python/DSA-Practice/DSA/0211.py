# DSA Problem 211

'''
Problem Statement:
A "lucky number" is defined as a positive integer that contains only the digits 4 and 7. Given a positive integer n, write a function `find_nearest_lucky` to find the nearest lucky number to n. If there are two lucky numbers equidistant from n, return the smaller one.

For example, 47 and 444 are lucky numbers, whereas 45 and 744778 are not.
'''

Solution:
```python
def find_nearest_lucky(n):
    def generate_lucky_numbers(length):
        if length == 1:
            return ['4', '7']
        else:
            shorter = generate_lucky_numbers(length - 1)
            return [digit + num for num in shorter for digit in ['4', '7']]
    
    def find_closest(lucky_numbers, target):
        closest = None
        min_diff = float('inf')
        for num in lucky_numbers:
            diff = abs(target - int(num))
            if diff < min_diff or (diff == min_diff and int(num) < closest):
                min_diff = diff
                closest = int(num)
        return closest
    
    length = len(str(n))
    lower = 10**(length - 1)
    upper = 10**length
    
    # Generate all possible lucky numbers within the range
    lucky_numbers = []
    for l in range(1, length + 2):  # Include one more length to ensure we find the nearest
        gen = generate_lucky_numbers(l)
        for g in gen:
            if lower <= int(g) < upper:
                lucky_numbers.append(int(g))
    
    return find_closest(lucky_numbers, n)

# Test the function
print(find_nearest_lucky(55))  # Example test case
```

This solution first generates all possible lucky numbers within a relevant range, then finds and returns the closest one to the input number `n`. The function `generate_lucky_numbers` recursively creates lucky numbers of a specified length, and `find_closest` finds the closest lucky number to the target number.