# DSA Problem 216

'''
Problem Statement:
A group of students is preparing for a programming competition. Each student has a skill level represented by a positive integer. The coach wants to form teams of exactly 3 students each, such that the skill level of the team is defined as the skill level of the weakest student in the team. The coach's goal is to maximize the total skill level of all teams combined. Given a list of the students' skill levels, write a function to return the maximum possible total skill level of all formed teams.

Note:
- There can be multiple teams formed, and each student can only be part of one team.
- If the number of students is not divisible by 3, some students may not be part of any team.
'''

Solution:
```python
def max_team_skill(skill_levels):
    """
    Calculate the maximum total skill level of teams formed from the given skill levels.
    
    :param skill_levels: List[int] - a list of integers representing the skill levels of students.
    :return: int - the maximum total skill level of all formed teams.
    """
    skill_levels.sort(reverse=True)
    total_skill = 0
    
    # Iterate through the sorted list, selecting every second student as the weakest link in the team
    for i in range(2, len(skill_levels), 3):
        total_skill += skill_levels[i]
        
    return total_skill

# Check function to verify the solution with provided data points
def check_solution():
    assert max_team_skill([1,3,5,2,2,2]) == 6, "Test case 1 failed"
    assert max_team_skill([2,6,5,2,4,5]) == 7, "Test case 2 failed"
    assert max_team_skill([1,2]) == 0, "Test case 3 failed"
    assert max_team_skill([10, 20, 30, 40, 50, 60]) == 90, "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```

This Python solution sorts the list of skill levels in descending order and then iterates through this list, summing up every third element (starting from the third element) to calculate the maximum total skill level of all formed teams, adhering to the problem's constraints.