# Python Question: Find the largest number that can be divided by any number from 1 to 10 without any remainder

'''
Input: A list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 512 (largest number that can be divided by 1 to 10 without any remainder)
'''

def find_largest_number_divisible_by(numbers):
    largest_number = 0
    for num in numbers:
        if num > largest_number and num % largest_number == 0:
            largest_number = num
    return largest_number

def test_find_largest_number_divisible_by():
    assert find_largest_number_divisible_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 512

if __name__ == "__main__":
    test_find_largest_number_divisible_by()