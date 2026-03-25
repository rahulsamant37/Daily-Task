def pow_mod(a, b, mod):
    """Fast modular exponentiation"""
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

def check_composite(n, a, d, s):
    """Check if n is composite using witness a"""
    x = pow_mod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    
    return True

def miller_rabin(n):
    """
    Miller-Rabin deterministic primality test
    Returns True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Deterministic witnesses for numbers up to certain bounds
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in witnesses:
        if n == a:
            return True
        if check_composite(n, a, d, s):
            return False
    
    return True

def is_prime(n):
    """Alias for miller_rabin for convenience"""
    return miller_rabin(n)

# Example usage and testing
def test_miller_rabin():
    """Test the Miller-Rabin implementation"""
    test_cases = [
        (2, True), (3, True), (4, False), (5, True),
        (17, True), (25, False), (97, True), (100, False),
        (1009, True), (1013, True), (1021, True), (1024, False)
    ]
    
    for num, expected in test_cases:
        result = miller_rabin(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"{num}: {result} (expected {expected}) - {status}")

if __name__ == "__main__":
    test_miller_rabin()
