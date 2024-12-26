# DSA Problem 298

'''
Problem Statement:
Given a list of integers, find the maximum value of the XOR operation between all unique pairs in the list. For example, if the list is [3, 10, 5, 25, 2, 8], one such pair could be (3, 10) where the XOR is 13. Your task is to calculate the maximum XOR value that can be obtained from any two distinct elements in the list. Note, the list can have up to 10^5 elements and each element can range from 0 to 10^9.

Hints:
- Consider using a bitwise approach to build a prefix tree (trie) for the numbers.
- Traverse the trie to find the maximum XOR value for each number by choosing the opposite bit at each step.
'''

Solution:
class TrieNode:
    def __init__(self):
        self.children = {}

def insert_number_in_trie(root, number):
    node = root
    for i in range(31, -1, -1):
        current_bit = (number >> i) & 1
        if current_bit not in node.children:
            node.children[current_bit] = TrieNode()
        node = node.children[current_bit]

def find_max_xor_pair(numbers):
    root = TrieNode()
    max_xor = 0
    for number in numbers:
        insert_number_in_trie(root, number)
        xor = 0
        node = root
        for i in range(31, -1, -1):
            current_bit = (number >> i) & 1
            opposite_bit = 1 - current_bit
            if opposite_bit in node.children:
                xor += (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[current_bit]
        max_xor = max(max_xor, xor)
    return max_xor

# Example usage
numbers = [3, 10, 5, 25, 2, 8]
print(find_max_xor_pair(numbers))  # Output will be the maximum XOR value from the given list.
'''

This solution constructs a trie to represent the binary representation of each number in the list. For each number in the list, it attempts to find a pair that maximizes the XOR value by navigating through the trie and choosing the opposite bit at each position to maximize the XOR.