# Python has built-in arbitrary precision integers
# No need for special 128-bit integer handling like in C++
# Python integers can handle numbers much larger than 1e36

# For very large number operations, you can use:
# - Built-in int type (arbitrary precision)
# - Decimal module for floating point precision
# - fractions module for exact rational arithmetic

from decimal import Decimal, getcontext

# Set precision for decimal operations (if needed)
def set_decimal_precision(precision=50):
    getcontext().prec = precision

# Example usage:
def large_number_demo():
    # Python can handle arbitrarily large integers natively
    large_num = 10**100  # This works perfectly in Python
    
    # For precise decimal operations
    set_decimal_precision(100)
    precise_decimal = Decimal('1') / Decimal('3')
    
    print(f"Large number: {large_num}")
    print(f"Precise decimal: {precise_decimal}")

# Utility functions for large numbers
def factorial_large(n):
    """Calculate factorial of large numbers"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power_large(base, exp):
    """Calculate base^exp for large numbers"""
    return base ** exp

def gcd_large(a, b):
    """GCD for large numbers"""
    while b:
        a, b = b, a % b
    return a

def lcm_large(a, b):
    """LCM for large numbers"""
    return (a * b) // gcd_large(a, b)

# Note: Python's int type automatically handles overflow
# No need for special overflow checking like in C++
