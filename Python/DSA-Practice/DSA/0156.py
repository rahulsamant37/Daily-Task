# DSA Problem 156

'''
Problem Statement:
You are given a list of integers representing the heights of buildings in a city. The city has a unique regulation that allows you to increase the height of any number of buildings by 1 meter, but only once. After this operation, you want to find the maximum number of consecutive buildings that have the same height.

For example, if the list of buildings is [1, 2, 2, 3, 3, 3], and you choose to increase the height of the first building, the list would become [2, 2, 2, 3, 3, 3]. Now, the maximum number of consecutive buildings with the same height is 3.

Write a function `max_consecutive_buildings` that takes a list of integers as input and returns the maximum number of consecutive buildings that can have the same height after performing the operation at most once.

Constraints:
- 1 <= len(buildings) <= 10^5
- 1 <= buildings[i] <= 10^9
'''

Solution:
```python
def max_consecutive_buildings(buildings):
    def longest_same_height(seq):
        count = {}
        max_length = 0
        start = 0
        
        for end in range(len(seq)):
            if seq[end] in count:
                count[seq[end]] += 1
            else:
                count[seq[end]] = 1
            
            while len(count) > 1:
                count[seq[start]] -= 1
                if count[seq[start]] == 0:
                    del count[seq[start]]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
    
    # Generate two new lists with the height of each building increased by 1 and 2 respectively
    plus_one = [x + 1 for x in buildings]
    plus_two = [x + 2 for x in buildings]
    
    # Calculate the longest sequence of the same height for the original, plus one, and plus two lists
    max_length = max(longest_same_height(buildings), longest_same_height(plus_one), longest_same_height(plus_two))
    
    return max_length

# Example usage
buildings = [1, 2, 2, 3, 3, 3]
print(max_consecutive_buildings(buildings))  # Output: 3
```

Note: The provided solution includes a helper function `longest_same_height` to find the longest subarray with the same elements in a given list. This approach considers the original list and the lists with incremented values by 1 and 2 to account for the allowed operation of increasing the height of buildings.