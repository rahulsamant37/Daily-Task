# Python Question: Find the largest number that can be formed using the digits of a given number without repetition

'''
For example, consider the number 5478. The largest number that can be formed from its digits without repetition is 5874.
'''

def largest_digit_number(num):
    # Sort the digits in descending order
    digits = sorted([int(digit) for digit in str(num)], reverse=True)
    
    # Join the sorted digits and return the result
    return ''.join(map(str, digits))

def test_largest_digit_number():
    assert largest_digit_number(1234) == '3412'
    assert largest_digit_number(6945) == '9569'
    assert largest_digit_number(1000) == '9991'
    assert largest_digit_number(8888) == '8888'
    assert largest_digit_number(123) == '321'
    assert largest_digit_number(4567) == '7654'
    assert largest_digit_number(123456789) == '987654321'

if __name__ == '__main__':
    test_largest_digit_number()