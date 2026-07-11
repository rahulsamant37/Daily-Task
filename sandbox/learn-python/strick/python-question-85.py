# Python Question: Print all prime numbers between 1 to 100
'''
Write a program to print all prime numbers between 1 to 100.

Example:
Input:
100
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''

def is_prime(number):
    if number < 2:  # prime number starts from 2
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def print_primes_between_1_to_100():
    primes = []
    for num in range(1, 101):
        if is_prime(num):
            primes.append(num)
    print(primes)

if __name__ == "__main__":
    print_primes_between_1_to_100()