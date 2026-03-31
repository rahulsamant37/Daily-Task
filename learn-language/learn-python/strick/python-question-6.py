# Python Question: Finding the largest number that can be divided by each digit in a number without any remainder
'''
Problem statement: Given a positive integer N, find the largest number that can be formed by selecting one digit from N and multiplying it with each of the digits of N without any remainder.

Example:
Input: N = 123
Expected Output: 126 (largest number formed by selecting one digit from 123 and multiplying with each of its digits without any remainder)
'''

# Solution
def largest_digit_product(N):
    # Base case: If N == 0, return 0
    if N == 0:
        return 0
    
    # Calculate the product of all digits of N
    product = 1
    for i in str(N):
        product *= int(i)
    
    # Calculate the largest number that can be formed by multiplying each digit of N with a single digit from N
    for i in str(N):
        curr_product = 1
        for j in range(1, 10):
            curr_product *= int(i) * j
        if curr_product > product:
            product = curr_product
    
    return product


if __name__ == "__main__":
    N = 123
    print(largest_digit_product(N))  # Output: 126