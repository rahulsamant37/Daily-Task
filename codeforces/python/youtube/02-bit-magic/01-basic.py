"""
Bitwise Operations in Python
----------------------------

Bitwise operations perform operations on binary representations of integers.
These operators work on bits and perform bit-by-bit operations.

Supported Bitwise Operators:

1. &  (AND)
   - Sets each bit to 1 if both bits are 1.
   - Example: 5 & 3 → 0b0101 & 0b0011 = 0b0001 → 1

2. |  (OR)
   - Sets each bit to 1 if one of the two bits is 1.
   - Example: 5 | 3 → 0b0101 | 0b0011 = 0b0111 → 7

3. ^  (XOR)
   - Sets each bit to 1 only if one of the two bits is 1 (but not both).
   - Example: 5 ^ 3 → 0b0101 ^ 0b0011 = 0b0110 → 6

4. ~  (NOT / One's Complement)
   - Inverts all the bits (i.e., changes 1s to 0s and 0s to 1s).
   - Example: ~5 → ~0b0101 = 0b...11111010 (2's complement) → -6

5. << (Left Shift)
   - Shifts bits to the left and fills 0s from the right.
   - Equivalent to multiplying the number by 2**n.
   - Example: 5 << 1 → 0b0101 << 1 = 0b1010 → 10

6. >> (Right Shift)
   - Shifts bits to the right and fills the left with the sign bit (for negative numbers).
   - Equivalent to integer division by 2**n.
   - Example: 5 >> 1 → 0b0101 >> 1 = 0b0010 → 2

Note:
- Bitwise operations are only defined for integers.
- Negative numbers are stored in 2's complement format.

Use these operations for low-level programming, performance optimizations,
bit masking, cryptography, or working with flags and hardware interfaces.
"""

# Bitwise AND to check even or odd
def even_odd(n):
    if n & 1 == 1:
        print(f"{n} is odd")
    else:
        print(f"{n} is even")

# Bitwise OR operation
def bitwise_or(a, b):
    result = a | b
    print(f"{a} | {b} = {result}")

# Bitwise XOR operation
def bitwise_xor(a, b):
    result = a ^ b
    print(f"{a} ^ {b} = {result}")

# Bitwise NOT operation
def bitwise_not(a):
    result = ~a
    print(f"~{a} = {result}")

# Bitwise Left Shift (Multiplication by 2^y)
def mul_power2(x, y):
    result = x << y
    print(f"{x} << {y} = {result}")

# Bitwise Right Shift (Division by 2^y)
def div_power2(x, y):
    result = x >> y
    print(f"{x} >> {y} = {result}")

# Example usage
if __name__ == "__main__":
    even_odd(5)
    even_odd(8)

    bitwise_or(5, 3)
    bitwise_xor(5, 3)
    bitwise_not(5)

    mul_power2(5, 1)
    div_power2(5, 1)
