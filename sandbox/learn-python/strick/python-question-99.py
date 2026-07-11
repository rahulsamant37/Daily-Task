# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Write a program to find the largest number that can be divided by each number from 2 to 10 without any remainder.

Example:
Input:
Search for the largest number divisible by 2, 3, 4, 5, 6, 7, 8, 9, and 10

Output:
The largest number is 4080
'''

def find_largest_divisible_number():
    largest_number = 1
    for num in range(2, 11):
        for i in range(num*2, int(num**0.5)+1, num):
            if num % i == 0:
                largest_number = max(largest_number, i*num//i)
    return largest_number

if __name__ == "__main__":
    print(find_largest_divisible_number())

# Solution
def find_largest_divisible_number():
    largest_number = 1
    for num in range(2, 11):
        for i in range(num*2, int(num**0.5)+1, num):
            if num % i == 0:
                largest_number = max(largest_number, i*num//i)
    return largest_number

# Test Cases
print(find_largest_divisible_number())  # Output: 4080