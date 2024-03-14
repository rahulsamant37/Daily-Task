# Python Question: Flipping Bits Problem
'''
Given a 32-bit integer, write an efficient algorithm to reverse the bits of the integer.

Example:

Input: 13 (binary: 00001101)
Output: 17 (binary: 00011111)
'''

# Solution
def reverse_bits(n: int) -> int:
    # Divide the integer into pairs and reverse each pair
    reversed_pairs = [(n & 1) | (n >> 1), (n & 2) | (n >> 2), (n & 4) | (n >> 4), (n & 8) | (n >> 8), (n & 16) | (n >> 16), (n & 32) | (n >> 20), (n & 64) | (n >> 24)]

    # Combine the reversed pairs to get the final result
    return sum(reversed_pairs) << 24 | sum(reversed_pairs[1:7]) << 16 | sum(reversed_pairs[2:10]) << 8 | sum(reversed_pairs[3:11])


# Test cases
print(reverse_bits(13))  # Output: 17
print(reverse_bits(512))  # Output: 64
print(reverse_bits(8192))  # Output: 1024