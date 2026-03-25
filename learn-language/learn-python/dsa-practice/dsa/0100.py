# DSA Problem 100

'''
Problem Statement:
You are given a list of integers representing the scores of participants in a competition. The competition has a unique rule: if a participant's score is equal to the average score of all participants, that participant is awarded a bonus point, increasing their score by 1. Write a function `adjust_scores` that takes in a list of integers and returns a new list where participants with scores equal to the average score have their scores incremented by 1, while others remain unchanged. Ensure the function handles the case where the input list is empty.

Example:
- adjust_scores([10, 20, 10, 30]) should return [11, 20, 11, 30]
- adjust_scores([]) should return []
'''

Solution:
```python
def adjust_scores(scores):
    """
    Adjusts the scores of participants based on the competition rule.
    
    :param scores: List of integers representing the scores of participants.
    :return: A new list with adjusted scores.
    """
    if not scores:
        return []
    
    average_score = sum(scores) / len(scores)
    return [int(score + 1) if score == average_score else score for score in scores]

# Check function to verify the correctness of the solution
def check_function():
    assert adjust_scores([10, 20, 10, 30]) == [11, 20, 11, 30], "Test case 1 failed"
    assert adjust_scores([]) == [], "Test case 2 failed"
    assert adjust_scores([5, 5, 5]) == [6, 6, 6], "Test case 3 failed"
    assert adjust_scores([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 4 failed"
    print("All test cases passed!")

# Running the check function to validate the solutions
check_function()
```

This code snippet defines a function `adjust_scores` that implements the described logic and a `check_function` to test the correctness of the solution.