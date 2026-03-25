# DSA Problem 96

'''
Problem Statement:
A group of students is participating in a coding competition. Each student has a unique skill level, represented by an integer. The organizers want to form teams such that the sum of the skill levels in each team is maximized, under the constraint that no team can have more than 3 members. Given a list of skill levels, find the maximum possible sum of skill levels across all formed teams.

For example, if the skill levels are [1, 3, 5, 9, 10], the optimal teams could be [1, 10] and [9, 5] with a total sum of 25.

Note:
- The length of the list will be between 1 and 100.
- Each element in the list will be an integer between 1 and 100.
'''

Solution:
```python
from typing import List

def max_team_sum(skill_levels: List[int]) -> int:
    """
    Returns the maximum possible sum of skill levels across all formed teams, given that no team can have more than 3 members.
    """
    skill_levels.sort(reverse=True)
    total_sum = 0
    for i in range(0, len(skill_levels), 3):
        for j in range(i, min(i + 3, len(skill_levels))):
            if (i - j) % 3 != 2:  # Exclude the third member in each block of three to maximize the sum
                total_sum += skill_levels[j]
    return total_sum

# Check function to verify the correctness of the solution
def check_solution():
    assert max_team_sum([1, 3, 5, 9, 10]) == 25, "Test case 1 failed"
    assert max_team_sum([10, 20, 30, 40, 50, 60]) == 180, "Test case 2 failed"
    assert max_team_sum([5, 4, 3, 2, 1]) == 12, "Test case 3 failed"
    assert max_team_sum([100]) == 100, "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```

This problem and solution are designed to challenge the contestant's ability to manipulate sorted data and apply a greedy algorithm to achieve the optimal solution under given constraints.