"""
Mathematical Optimizations and Bit Tricks
=========================================

Fast mathematical operations and bit manipulations for competitive programming.
"""

import math

def fast_power_operations():
    """
    Optimized power and modular arithmetic
    """
    MOD = 10**9 + 7
    
    # Fast modular exponentiation
    def fast_pow(base, exp, mod):
        return pow(base, exp, mod)  # Built-in is optimized
    
    # BAD: (base ** exp) % mod - can overflow
    def slow_pow(base, exp, mod):
        return (base ** exp) % mod
    
    # Modular multiplication
    def mod_mul(a, b, mod):
        return (a * b) % mod
    
    # Precompute powers for repeated use
    def precompute_powers(base, max_exp, mod):
        powers = [1] * (max_exp + 1)
        for i in range(1, max_exp + 1):
            powers[i] = (powers[i-1] * base) % mod
        return powers
    
    return fast_pow(2, 10, MOD), precompute_powers(2, 20, MOD)

def bit_manipulation_tricks():
    """
    Essential bit manipulation operations
    """
    
    # Check if number is power of 2
    def is_power_of_2(n):
        return n > 0 and (n & (n - 1)) == 0
    
    # Get i-th bit (0-indexed from right)
    def get_bit(n, i):
        return (n >> i) & 1
    
    # Set i-th bit
    def set_bit(n, i):
        return n | (1 << i)
    
    # Clear i-th bit
    def clear_bit(n, i):
        return n & ~(1 << i)
    
    # Toggle i-th bit
    def toggle_bit(n, i):
        return n ^ (1 << i)
    
    # Count number of 1s in binary representation
    def count_bits(n):
        # Python 3.10+
        if hasattr(n, 'bit_count'):
            return n.bit_count()
        else:
            return bin(n).count('1')
    
    # Get rightmost set bit
    def rightmost_set_bit(n):
        return n & (-n)
    
    # Remove rightmost set bit
    def remove_rightmost_set_bit(n):
        return n & (n - 1)
    
    return {
        'is_power_of_2_8': is_power_of_2(8),
        'get_bit_5_pos_2': get_bit(5, 2),  # 101, bit at pos 2 is 1
        'count_bits_7': count_bits(7),     # 111 has 3 bits
        'rightmost_set_12': rightmost_set_bit(12)  # 1100 -> 100 (4)
    }

def fast_math_operations():
    """
    Optimized mathematical computations
    """
    
    # Fast integer square root
    def fast_sqrt(n):
        return math.isqrt(n)  # Python 3.8+
    
    # Fast GCD and LCM
    def fast_gcd_lcm(a, b):
        g = math.gcd(a, b)
        l = (a * b) // g
        return g, l
    
    # Divmod is faster than separate // and %
    def fast_divmod(a, b):
        quotient, remainder = divmod(a, b)
        return quotient, remainder
    
    # Precompute factorials for combinatorics
    def precompute_factorials(n, mod):
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i-1] * i) % mod
        return fact
    
    # Modular inverse using Fermat's little theorem
    def mod_inverse(a, mod):
        return pow(a, mod - 2, mod)  # Works when mod is prime
    
    return {
        'sqrt_100': fast_sqrt(100),
        'gcd_lcm_12_8': fast_gcd_lcm(12, 8),
        'divmod_17_5': fast_divmod(17, 5),
        'factorials_10': precompute_factorials(10, 10**9 + 7)[:11]
    }

def number_theory_functions():
    """
    Common number theory functions for CP
    """
    
    # Sieve of Eratosthenes (optimized)
    def sieve_of_eratosthenes(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        
        return [i for i in range(2, n + 1) if sieve[i]]
    
    # Prime factorization
    def prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    return {
        'primes_up_to_30': sieve_of_eratosthenes(30),
        'factors_of_60': prime_factors(60),
        'extended_gcd_35_15': extended_gcd(35, 15)
    }

def combinatorics_functions():
    """
    Combinatorics with modular arithmetic
    """
    MOD = 10**9 + 7
    
    def nCr_mod(n, r, mod):
        if r > n or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        
        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i-1] * i) % mod
        
        # nCr = n! / (r! * (n-r)!)
        numerator = fact[n]
        denominator = (fact[r] * fact[n-r]) % mod
        
        # Modular inverse
        inv_denominator = pow(denominator, mod - 2, mod)
        
        return (numerator * inv_denominator) % mod
    
    return nCr_mod(10, 3, MOD)  # 10C3 = 120

def optimization_tips():
    """
    Key optimization principles
    """
    tips = [
        "Use pow(base, exp, mod) instead of (base ** exp) % mod",
        "Use math.gcd, math.isqrt for built-in optimized functions",
        "Precompute factorials, powers, and other repeated calculations",
        "Use bit operations (<<, >>, &, |, ^) when possible",
        "divmod(a, b) is faster than separate a // b and a % b",
        "Use bin(n).count('1') or n.bit_count() for counting bits",
        "n & (n-1) removes rightmost set bit",
        "n & -n gets rightmost set bit",
        "n & 1 checks if odd, n >> 1 divides by 2"
    ]
    return tips

if __name__ == "__main__":
    print("Mathematical Optimizations for CP")
    
    # Test power operations
    result, powers = fast_power_operations()
    print(f"Fast power result: {result}")
    print(f"Precomputed powers of 2: {powers[:10]}")
    
    # Test bit operations
    bit_results = bit_manipulation_tricks()
    print(f"Bit manipulation results: {bit_results}")
    
    # Test math operations
    math_results = fast_math_operations()
    print(f"Math operations: {math_results}")
    
    # Test number theory
    nt_results = number_theory_functions()
    print(f"Number theory: {nt_results}")
    
    # Test combinatorics
    comb_result = combinatorics_functions()
    print(f"10C3 = {comb_result}")
    
    # Show tips
    tips = optimization_tips()
    print("\nOptimization Tips:")
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
