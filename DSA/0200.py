# DSA Problem 200

'''
Problem Statement:
You are tasked with organizing a series of workshops, each requiring a specific number of participants. You have a list of available groups, each with a distinct number of members. Your goal is to match each workshop to a group so that the total happiness is maximized. The happiness of a workshop-group match is defined as the product of the number of participants required for the workshop and the number of members in the group. Each group can be used for at most one workshop. If there are not enough groups to cover all workshops, some workshops will be canceled, reducing the overall happiness. Find the maximum possible total happiness.

For example, if you have workshops requiring [2, 3, 4] participants and available groups of sizes [3, 4, 5], the optimal matching would be to match the first workshop with the first group, the second workshop with the second group, and the third workshop with the third group, resulting in a total happiness of 2*3 + 3*4 + 4*5 = 38.
'''

Solution:
```python
from typing import List

def max_happiness(workshops: List[int], groups: List[int]) -> int:
    """
    Calculate the maximum possible total happiness by optimally matching workshops to groups.
    """
    # Sort both lists in ascending order to maximize the product of matches
    workshops.sort()
    groups.sort()
    
    # Calculate the total happiness by matching each workshop to a group
    total_happiness = sum(workshop * group for workshop, group in zip(workshops, groups))
    
    return total_happiness

# Check function to verify the solution with provided data points
def check_solution():
    assert max_happiness([2, 3, 4], [3, 4, 5]) == 38, "Test case 1 failed"
    assert max_happiness([1, 2], [4, 3]) == 10, "Test case 2 failed"
    assert max_happiness([6], [1]) == 6, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python solution includes a function `max_happiness` that takes two lists as input: `workshops` and `groups`, and returns the maximum possible total happiness. The solution is verified with a `check_solution` function that tests the solution against predefined test cases.