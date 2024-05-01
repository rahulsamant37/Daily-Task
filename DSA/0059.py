# DSA Problem 59

'''
Problem Statement:
A group of students are participating in a coding competition where they need to solve a series of challenges. The challenges are numbered from 1 to N, and each challenge has a difficulty level, represented by a positive integer. The students can choose any challenge to start with, but once they start a challenge, they must solve it before moving on to the next one. The students can only move to the next challenge if the difficulty level of the next challenge is greater than the current one.

Your task is to help the students by finding the longest sequence of challenges they can solve in order of increasing difficulty. You are to return the length of this sequence.

For example:
- If the challenges have difficulty levels [2, 3, 1, 4, 5], the longest sequence would be [1, 4, 5], so the function should return 3.
- If the challenges have difficulty levels [10, 9, 2, 5, 3, 7, 101, 18], the longest sequence would be [2, 3, 7, 101], so the function should return 4.
'''

Solution:
def longest_increasing_sequence(challenges):
    """
    Finds the length of the longest strictly increasing subsequence in a list of integers.
    :param challenges: List[int] representing the difficulty levels of challenges.
    :return: Integer representing the length of the longest strictly increasing subsequence.
    """
    n = len(challenges)
    dp = [1] * n  # Initialize the DP array with 1s, as the minimum length of LIS ending at each index is 1.
    
    for i in range(1, n):
        for j in range(i):
            if challenges[i] > challenges[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)  # The length of the longest increasing subsequence.

# Check function to verify the correctness of the solution
def check():
    assert longest_increasing_sequence([2, 3, 1, 4, 5]) == 3
    assert longest_increasing_sequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_sequence([5, 4, 3, 2, 1]) == 1
    assert longest_increasing_sequence([1, 2, 3, 4, 5]) == 5
    print("All test cases passed successfully.")

check()
# Run the check function to validate the solution against the provided test cases.
