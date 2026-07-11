# Python Question: Finding the largest number that can be divided evenly by each digit from 1 to 9
'''
In this problem, we need to find the largest number that can be divided evenly by each digit from 1 to 9. We can use a loop to iterate through each digit and check if the number is divisible by it. If it is, we update the result.
For example, consider the number 456. We will check if 456 is divisible by each digit from 1 to 9 one by one.
1. Check if 456 is divisible by 1: False (456 % 1 == 0)
2. Check if 456 is divisible by 2: True (456 % 2 == 0)
3. Check if 456 is divisible by 3: True (456 % 3 == 0)
4. Check if 456 is divisible by 4: False (456 % 4 == 0)
5. Check if 456 is divisible by 5: True (456 % 5 == 0)
6. Check if 456 is divisible by 6: True (456 % 6 == 0)
7. Check if 456 is divisible by 7: False (456 % 7 == 0)
8. Check if 456 is divisible by 8: True (456 % 8 == 0)
9. Check if 456 is divisible by 9: True (456 % 9 == 0)
10. Check if 456 is divisible by 10: True (456 % 10 == 0)

The largest number among these is 456.
'''

def largest_number(digits):
    result = 0
    for digit in digits:
        for i in range(10):
            result = max(result, digit * 10 ** i)
    return result

def main():
    digits = [str(x) for x in range(1, 101) if str(x) not in ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']]
    print(largest_number(digits))

if __name__ == "__main__":
    main()