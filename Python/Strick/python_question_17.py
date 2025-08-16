# Python Question: Find the largest number that can be divided by each number from 1 to 10 without any remainder

'''
You are given a list of positive integers. Find the largest number among them that can be evenly divided by each of the given numbers without leaving a remainder.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 5 (Since 5 can be divided without any remainder by 1, 2, 3, 4, 6, 7, 8, 9, and 10)
'''

def find_largest_divisible_by(numbers):
    # Find the product of all numbers
    product = 1
    for num in numbers:
        product *= num
    
    # Find the numbers that divide product exactly
    possible_divisors = []
    for i in range(1, product+1):
        if numbers.count(i) > 0:
            possible_divisors.append(i)
    
    # Find the largest number among the possible divisors
    largest_divisible = possible_divisors[0]
    for divisor in possible_divisors:
        if divisor > largest_divisible:
            largest_divisible = divisor
    
    return largest_divisible

def test_find_largest_divisible_by():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_largest_divisible_by(numbers) == 5, "Expected the program to return 5 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by(numbers) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [1, 2, 3, 4, 5]
    assert find_largest_divisible_by(numbers) == 5, "Expected the program to return 5 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by([10]) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by([10]))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by(numbers) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by(numbers) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by(numbers) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by(numbers))
    numbers = [10, 20, 30, 40, 50]
    assert find_largest_divisible_by(numbers) == 10, "Expected the program to return 10 but got {}".format(find_largest_divisible_by(numbers))