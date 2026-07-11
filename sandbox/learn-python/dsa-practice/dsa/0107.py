# DSA Problem 107

'''
Problem Statement:
A "bouncy" number is defined as a positive integer that is neither strictly increasing nor strictly decreasing. For example, 123 is not bouncy (it's increasing), 321 is not bouncy (it's decreasing), but 155349 is bouncy. Find the least number for which the proportion of bouncy numbers is exactly 99%.

Note:
- The number should be greater than 99.
- You need to return the smallest number for which 99% of the numbers below it are bouncy.
'''

Solution:
def is_bouncy(num):
    num_str = str(num)
    increasing = all(num_str[i] <= num_str[i+1] for i in range(len(num_str)-1))
    decreasing = all(num_str[i] >= num_str[i+1] for i in range(len(num_str)-1))
    return not increasing and not decreasing

def find_least_bouncy():
    bouncy_count = 0
    total = 99
    for n in range(100, 1000000):  # Arbitrarily large upper limit
        if is_bouncy(n):
            bouncy_count += 1
        total += 1
        if bouncy_count / total == 0.99:
            return n

print(find_least_bouncy())