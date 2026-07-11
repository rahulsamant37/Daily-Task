import sys
import math
import random
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import time

# Fast I/O
input = sys.stdin.readline

# Constants
MOD = 1000000007
MOD1 = 998244353
INF = float('inf')
PI = math.pi

# Debug flag - set to True for local testing
DEBUG = False

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def pow_mod(a, b, mod=MOD):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

def mod_inverse(a, mod=MOD):
    return pow_mod(a, mod - 2, mod)

def mod_add(a, b, mod=MOD):
    return ((a % mod) + (b % mod)) % mod

def mod_sub(a, b, mod=MOD):
    return ((a % mod) - (b % mod) + mod) % mod

def mod_mul(a, b, mod=MOD):
    return ((a % mod) * (b % mod)) % mod

def mod_div(a, b, mod=MOD):
    return mod_mul(a, mod_inverse(b, mod), mod)

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return primes

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

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve():
    pass

def main():
    if DEBUG:
        sys.stderr = open('error.txt', 'w')
    
    start_time = time.time()
    solve()
    
    if DEBUG:
        end_time = time.time()
        print(f"Time: {(end_time - start_time) * 1000:.0f}ms", file=sys.stderr)

if __name__ == "__main__":
    main()
