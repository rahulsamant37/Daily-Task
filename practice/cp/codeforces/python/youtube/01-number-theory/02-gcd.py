import math

r"""
| Method                | Time Complexity          | Space Complexity      | Notes                       |
| --------------------- | ------------------------ | --------------------- | --------------------------- |
| `math.gcd(a, b)`      | O(log(min(a, b)))        | O(1)                  | Fastest and most efficient  |
| Euclidean (Iterative) | O(log(min(a, b)))        | O(1)                  | Great for custom logic      |
"""

a = 10
b = 3

## O(log(min(a, b))), O(1)
print(math.gcd(a,b))

## O(log(min(a, b))), O(1)
def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a
print(gcd(a,b))