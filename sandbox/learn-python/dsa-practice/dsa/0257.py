# DSA Problem 257

'''
Problem Statement:
A company needs to organize a meeting and has a list of employees who are required to attend. However, the meeting room can only accommodate up to 50 people at a time. The company decides to split the meeting into multiple sessions, each session not exceeding 50 attendees. Given a list of employee IDs, write a function `organize_sessions(employees)` that returns the minimum number of sessions needed to accommodate all employees. Each session must be as full as possible without exceeding 50 people, and every employee must attend exactly one session.

For example, if there are 113 employees, the function would need to return 3 because 2 sessions can hold 100 employees (50 each), and the third session will hold the remaining 13 employees.
'''

Solution:
```python
def organize_sessions(employees):
    """
    Calculates the minimum number of sessions required to accommodate all employees
    in a meeting room that can hold up to 50 people at a time.
    
    :param employees: List of employee IDs
    :return: Minimum number of sessions needed
    """
    num_employees = len(employees)
    return (num_employees + 49) // 50  # Integer division, rounding up

# Checking function to test the solution
def check_solution():
    assert organize_sessions(list(range(100))) == 2, "Test case 1 failed"
    assert organize_sessions(list(range(150))) == 3, "Test case 2 failed"
    assert organize_sessions(list(range(1))) == 1, "Test case 3 failed"
    assert organize_sessions(list(range(50))) == 1, "Test case 4 failed"
    assert organize_sessions(list(range(151))) == 4, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This code snippet defines a function `organize_sessions` that calculates the minimum number of sessions required to ensure all employees can attend a meeting, given constraints on the meeting room capacity. It also includes a `check_solution` function to verify the correctness of the solution with different input sizes.