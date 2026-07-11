# DSA Problem 171

'''
Problem Statement:
A group of friends decide to play a game where each person writes down a positive integer on a piece of paper. The game's goal is to find the friend who has the smallest unique number. If there is no such number, the game is considered a draw. Given a list of integers representing the numbers chosen by the friends, write a function to determine the winner of the game and return their number. If the game is a draw, return -1.

Example:
Input: [3, 3, 2, 1, 2]
Output: 1
Explanation: The smallest unique number is 1, hence the winner is the friend with the number 1.

Input: [4, 4, 4, 4]
Output: -1
Explanation: There are no unique numbers, the game is a draw.
'''

Solution:
```python
def find_smallest_unique(nums):
    # Create a dictionary to count occurrences of each number
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Filter out numbers that are not unique (occurred more than once)
    unique_nums = [num for num in count if count[num] == 1]
    
    # Check if there are any unique numbers
    if not unique_nums:
        return -1
    
    # Return the smallest unique number
    return min(unique_nums)

# Test cases
print(find_smallest_unique([3, 3, 2, 1, 2]))  # Output: 1
print(find_smallest_unique([4, 4, 4, 4]))     # Output: -1
```

This Python solution efficiently identifies the smallest unique number according to the problem statement. It uses a dictionary to count the occurrences of each number and then filters out the numbers that are not unique before returning the smallest unique number or -1 if there is no unique number.