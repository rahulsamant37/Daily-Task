# Python Question: Calculate the largest number that can be divided by each digit from 1 to 9 without any remainder
'''
In this problem, we are given a positive integer and the goal is to find the largest number that can be formed by dividing the given number using each digit from 1 to 9 without any remainder.

For example, consider the number 456. The largest numbers obtained by dividing 456 using each digit from 1 to 9 without any remainder are:
8 = 456 / 8 = 57
9 = 456 / 9 = 50
1 = 456 / 1 = 456
2 = 456 / 2 = 228
3 = 456 / 3 = 152
4 = 456 / 4 = 114
5 = 456 / 5 = 91
6 = 456 / 6 = 76
7 = 456 / 7 = 65 (The remainder is 1)
8 = 456 / 8 = 57 (The remainder is 4)
9 = 456 / 9 = 49 (The remainder is 5)

The largest number among the above numbers is 987654321.
'''

def find_largest_digit_divisible_number(number):
    digits = [int(digit) for digit in str(number)]

    result = 1
    for digit in digits:
        remainder = number // digit
        if remainder == 0:
            result *= digit
            number -= digit * remainder

    return result

if __name__ == '__main__':
    number = 456
    print(find_largest_digit_divisible_number(number))