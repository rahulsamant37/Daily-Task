# DSA Problem 14

'''
Problem Statement:
In a game, a player can move on a number line starting from 0. The player has an energy level represented by an integer E. At each step, the player can move to the right by 1 unit if they spend 1 energy, or to the left by 1 unit if they spend 2 energy. The goal is to reach a specific position P on the number line using the least amount of energy. If the player cannot reach position P with the given energy, return -1.

For example, to reach position 3, the player could move right three times using 3 energy. To reach position -2, the player could move left twice using 4 energy.
'''

Solution:
```python
def min_energy_to_reach_position(P, E):
    """
    Calculate the minimum energy required to reach position P.
    """
    # If P is positive, the most efficient way is to move right P times.
    # If P is negative, the best strategy is to move right and then move left to reach P.
    if P >= 0:
        if P > E:
            return -1
        else:
            return P
    else:
        P = abs(P)
        if P > E:
            return -1
        elif (E - P) % 2 == 0:
            return E
        else:
            return -1

# Check function to verify the solution with provided data points
def check():
    assert min_energy_to_reach_position(3, 5) == 3
    assert min_energy_to_reach_position(-2, 4) == 4
    assert min_energy_to_reach_position(1, 1) == 1
    assert min_energy_to_reach_position(-3, 5) == -1
    assert min_energy_to_reach_position(5, 10) == 5
    print("All test cases passed.")

check()
```

This solution calculates the minimum energy needed to reach a given position on a number line, considering the different costs of moving left and right. It checks if reaching the target position is even possible with the given energy level and returns the minimum energy required or -1 if it's not possible.