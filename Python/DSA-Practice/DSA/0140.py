# DSA Problem 140

'''
Problem Statement:
Given a list of integers, write a function `find_unique_pairs` that returns the number of unique, unordered pairs of elements from the list that sum up to a specific target value. Each element in the list can only be used once in a pair.

For example, given the list [1, 3, 2, 2, 3, 4] and the target sum of 5, the function should return 3 because there are three unique pairs that sum up to 5: (1, 4), (3, 2), and (3, 2). Note that (3, 2) and (2, 3) are considered the same pair due to the unordered nature.

Constraints:
- The list can have up to 1000 elements.
- Each element in the list is a positive integer.
- The target sum is a positive integer.
- The function should be efficient even with large lists.
'''

Solution:
def find_unique_pairs(nums, target):
    from collections import Counter
    
    # Count the occurrences of each number in the list
    num_counts = Counter(nums)
    count = 0
    used = set()
    
    for num in num_counts:
        complement = target - num
        if complement in num_counts and (complement, num) not in used and (num, complement) not in used:
            if complement != num:
                count += 1
                used.add((num, complement))
            else:
                # If the number is exactly half of the target, ensure there are at least two instances
                if num_counts[num] > 1:
                    count += 1
                    used.add((num, complement))
    
    return count

# Example usage:
# pairs = find_unique_pairs([1, 3, 2, 2, 3, 4], 5)
# print(pairs)  # Output: 3
# The pairs are (1, 4), (3, 2), and (3, 2). Note that the pair (3, 2) is only counted once.
'''

This problem requires an understanding of hashing and the ability to handle potential edge cases, such as counting a pair only once when the target sum can be divided evenly between two identical numbers in the list. The solution efficiently counts occurrences of each number and checks for pairs that sum up to the target value, ensuring each pair is counted only once.