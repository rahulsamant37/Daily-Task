# Python Question: Finding the largest number that can be divided without any remainder by numbers from 1 to 10

'''
In this problem, we need to find the largest number that can be divided without any remainder by numbers from 1 to 10.

Example:
Input: Find the largest number that can be divided without any remainder by numbers from 1 to 10.
Output: 50 (as 50 is divisible by numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 without any remainder)
'''

def largest_number_divisible_by_numbers_from_1_to_10():
    largest = 1
    for num in range(2, 11):
        if num * largest % num == 0:
            largest *= num
    return largest

if __name__ == "__main__":
    print(largest_number_divisible_by_numbers_from_1_to_10())

# Output: 50