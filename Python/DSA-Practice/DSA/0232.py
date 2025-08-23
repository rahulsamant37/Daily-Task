# DSA Problem 232

'''
Problem Statement:
You are given an array `arr` of positive integers. Write a function `find_lucky_triples` that finds the number of lucky triples `(arr[i], arr[j], arr[k])` in `arr`. A triple is considered lucky if the following conditions are met:
- `0 <= i < j < k < arr.length`
- `arr[i]` divides `arr[j]` and `arr[j]` divides `arr[k]` evenly.

For example, if `arr = [1, 2, 3, 4, 5, 6]`, one lucky triple would be `(1, 2, 4)` because `1` divides `2` and `2` divides `4`.

Constraints:
- The length of `arr` is at most 2000.
- All elements of `arr` will be between 1 and 10^6, inclusive.
'''

Solution:
```python
def find_lucky_triples(arr):
    n = len(arr)
    count = [0] * n
    result = 0
    
    for k in range(n):
        for j in range(k):
            if arr[k] % arr[j] == 0:  # arr[j] divides arr[k]
                count[k] += 1
                result += count[j]
                
    return result

# Example usage
arr = [1, 2, 3, 4, 5, 6]
print(find_lucky_triples(arr))  # Output depends on the input array.
```

This function iterates through the array, tracking how many numbers divide the current number and using this information to count the lucky triples. It leverages dynamic counting to optimize the calculation of lucky triples.