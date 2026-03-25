# DSA Problem 24

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum number of unique integers you can have in the list if you are allowed to change up to `k` elements in the list to any value. 

For example, if `nums = [1, 2, 3, 4, 5, 6]` and `k = 2`, you could change two of the numbers to any other numbers, aiming to maximize the number of unique numbers in the list.

Your task is to implement a function `maxUniqueIntegers(nums, k)` that returns the maximum number of unique integers you can achieve under the given constraints.
'''

Solution:
```python
def maxUniqueIntegers(nums, k):
    from collections import Counter
    
    # Count the frequency of each number
    freq = Counter(nums)
    # Find the frequency of frequencies
    freq_of_freq = Counter(freq.values())
    
    unique_count = len(freq)  # Initial count of unique numbers
    
    # We iterate over possible frequencies, starting from the least frequent
    for f in range(1, len(nums) + 1):
        if k <= 0:
            break
        # If there are numbers with frequency f, we try to change some of them
        while freq_of_freq[f] > 0 and k > 0:
            # We can decrease the frequency of the number by 1 (change one occurrence)
            k -= 1
            freq_of_freq[f] -= 1  # One number with frequency f is now with frequency f-1
            freq_of_freq[f - 1] += 1  # Update the frequency-of-frequencies
            if f == 1:
                unique_count -= 1  # If we change a unique number, the unique count decreases
        if k <= 0:
            break
    
    return unique_count

# Example check:
print(maxUniqueIntegers([1, 2, 3, 4, 5, 6], 2))  # Expected output: 6
print(maxUniqueIntegers([1, 2, 2, 2, 3, 4], 2))  # Expected output: 5
```

This solution counts the frequency of each number in the list and then strategizes to maximize the number of unique integers by changing as few numbers as possible. The `Counter` from the `collections` module is used to facilitate counting and manipulating frequencies.