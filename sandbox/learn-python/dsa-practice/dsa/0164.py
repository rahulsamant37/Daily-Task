# DSA Problem 164

'''
Problem Statement:
Alice and Bob are playing a game with a list of integers. Alice chooses a number from the list, and Bob must find the next largest number in the list that is a multiple of the chosen number. If there is no such number, Bob loses. Given a list of integers and Alice's chosen number, write a function to determine if Bob can win the game and return the winning number if possible. Assume all numbers in the list are positive integers and the list contains at least two elements.

Example:
For the list [2, 4, 6, 8, 10] and Alice's chosen number as 2, the function should return 4 as it is the next largest multiple of 2 in the list.
'''

Solution:
def find_next_multiple(nums, alice_choice):
    """
    Finds the next largest number in the list that is a multiple of the chosen number.
    If no such number exists, returns -1.
    """
    nums.sort()
    for num in nums:
        if num > alice_choice and num % alice_choice == 0:
            return num
    return -1

# Example check function
def check_solution():
    assert find_next_multiple([2, 4, 6, 8, 10], 2) == 4
    assert find_next_multiple([1, 2, 3, 4, 5], 5) == -1
    assert find_next_multiple([3, 6, 9, 12, 15], 3) == 6
    print("All tests passed!")

check_solution()
# This solution first sorts the list to ensure that the numbers are in ascending order,
# then iterates through the list to find the smallest number greater than the chosen number
# that is also a multiple of it. If such a number is found, it is returned; otherwise, -1 is returned.