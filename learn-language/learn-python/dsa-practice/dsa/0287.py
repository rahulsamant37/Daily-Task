# DSA Problem 287

'''
Problem Statement:
You are given a list of positive integers representing the heights of buildings. A building can see the sunrise if there is no taller building to its east (right side). Your task is to find the number of buildings that can see the sunrise.

For example, if the buildings' heights are [4, 2, 3, 1], then the buildings with heights 4 and 3 can see the sunrise, so the answer would be 2.
'''

Solution:
def can_see_sunrise(buildings):
    """
    Counts how many buildings can see the sunrise.
    
    :param buildings: List of integers representing the heights of buildings
    :return: Integer representing the number of buildings that can see the sunrise
    """
    if not buildings:
        return 0
    
    count = 1  # The rightmost building always sees the sunrise.
    max_height = buildings[-1]
    
    for height in reversed(buildings[:-1]):
        if height > max_height:
            count += 1
            max_height = height
            
    return count

# Test cases
print(can_see_sunrise([3, 7, 5, 6, 8]))  # Expected output: 2
print(can_see_sunrise([4, 2, 3, 1]))     # Expected output: 2
print(can_see_sunrise([2, 3, 6, 1]))     # Expected output: 3
print(can_see_sunrise([1]))              # Expected output: 1
print(can_see_sunrise([]))               # Expected output: 0