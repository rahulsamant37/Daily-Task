MOD = 1000000007

def matrix_multiply(A, B):
    """Multiply two 2x2 matrices"""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= MOD
    return result

def matrix_power(matrix, n):
    """Compute matrix^n using fast exponentiation"""
    if n == 0:
        return [[1, 0], [0, 1]]  # Identity matrix
    
    if n == 1:
        return [row[:] for row in matrix]  # Copy of matrix
    
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

def nth_fibonacci(n):
    """
    Calculate nth Fibonacci number in O(log n) time
    F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, ...
    """
    if n <= 1:
        return n
    
    # Base transformation matrix
    # [F(n), F(n-1)] = [F(n-1), F(n-2)] * [[1, 1], [1, 0]]
    base_matrix = [[1, 1], [1, 0]]
    
    # Compute base_matrix^(n-1)
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # [F(n), F(n-1)] = [F(1), F(0)] * base_matrix^(n-1)
    # F(n) = F(1) * result_matrix[0][0] + F(0) * result_matrix[1][0]
    # F(n) = 1 * result_matrix[0][0] + 0 * result_matrix[1][0]
    return result_matrix[0][0]

def fibonacci_modular(n, mod=MOD):
    """Calculate nth Fibonacci number modulo mod"""
    if n <= 1:
        return n
    
    base_matrix = [[1, 1], [1, 0]]
    
    def matrix_mult_mod(A, B, mod):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += A[i][k] * B[k][j]
                    result[i][j] %= mod
        return result
    
    def matrix_pow_mod(matrix, n, mod):
        if n == 0:
            return [[1, 0], [0, 1]]
        if n == 1:
            return [row[:] for row in matrix]
        
        if n % 2 == 0:
            half = matrix_pow_mod(matrix, n // 2, mod)
            return matrix_mult_mod(half, half, mod)
        else:
            return matrix_mult_mod(matrix, matrix_pow_mod(matrix, n - 1, mod), mod)
    
    result_matrix = matrix_pow_mod(base_matrix, n - 1, mod)
    return result_matrix[0][0]

# Extended applications of matrix exponentiation

def tribonacci(n):
    """
    Calculate nth Tribonacci number: T(n) = T(n-1) + T(n-2) + T(n-3)
    T(0) = 0, T(1) = 0, T(2) = 1
    """
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    
    # Transformation matrix for tribonacci
    # [T(n), T(n-1), T(n-2)] = [T(n-1), T(n-2), T(n-3)] * matrix
    base_matrix = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    
    def matrix_mult_3x3(A, B):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += A[i][k] * B[k][j]
                    result[i][j] %= MOD
        return result
    
    def matrix_pow_3x3(matrix, n):
        if n == 0:
            return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        if n == 1:
            return [row[:] for row in matrix]
        
        if n % 2 == 0:
            half = matrix_pow_3x3(matrix, n // 2)
            return matrix_mult_3x3(half, half)
        else:
            return matrix_mult_3x3(matrix, matrix_pow_3x3(matrix, n - 1))
    
    result_matrix = matrix_pow_3x3(base_matrix, n - 2)
    # T(n) = T(2) * result[0][0] + T(1) * result[0][1] + T(0) * result[0][2]
    # T(n) = 1 * result[0][0] + 0 * result[0][1] + 0 * result[0][2]
    return result_matrix[0][0]

def linear_recurrence(coeffs, initial, n):
    """
    Solve linear recurrence relation using matrix exponentiation
    a(n) = c1*a(n-1) + c2*a(n-2) + ... + ck*a(n-k)
    
    Args:
        coeffs: [c1, c2, ..., ck] coefficients
        initial: [a(0), a(1), ..., a(k-1)] initial values
        n: target index
    
    Returns:
        a(n)
    """
    k = len(coeffs)
    if n < k:
        return initial[n]
    
    # Build transformation matrix
    matrix = [[0] * k for _ in range(k)]
    # First row: coefficients
    matrix[0] = coeffs[:]
    # Other rows: shift matrix
    for i in range(1, k):
        matrix[i][i-1] = 1
    
    def matrix_mult_kxk(A, B):
        size = len(A)
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for l in range(size):
                    result[i][j] += A[i][l] * B[l][j]
                    result[i][j] %= MOD
        return result
    
    def matrix_pow_kxk(matrix, n):
        size = len(matrix)
        if n == 0:
            # Identity matrix
            identity = [[0] * size for _ in range(size)]
            for i in range(size):
                identity[i][i] = 1
            return identity
        
        if n == 1:
            return [row[:] for row in matrix]
        
        if n % 2 == 0:
            half = matrix_pow_kxk(matrix, n // 2)
            return matrix_mult_kxk(half, half)
        else:
            return matrix_mult_kxk(matrix, matrix_pow_kxk(matrix, n - 1))
    
    result_matrix = matrix_pow_kxk(matrix, n - k + 1)
    
    # Calculate result
    result = 0
    for i in range(k):
        result += result_matrix[0][k-1-i] * initial[k-1-i]
        result %= MOD
    
    return result

# Test functions
def test_fibonacci():
    """Test fibonacci implementation"""
    print("Testing Fibonacci:")
    for i in range(10):
        print(f"F({i}) = {nth_fibonacci(i)}")

def test_tribonacci():
    """Test tribonacci implementation"""
    print("\nTesting Tribonacci:")
    for i in range(10):
        print(f"T({i}) = {tribonacci(i)}")

def test_linear_recurrence():
    """Test linear recurrence"""
    print("\nTesting Linear Recurrence (Fibonacci):")
    # Fibonacci: a(n) = a(n-1) + a(n-2)
    coeffs = [1, 1]
    initial = [0, 1]
    for i in range(10):
        result = linear_recurrence(coeffs, initial, i)
        expected = nth_fibonacci(i)
        print(f"LR F({i}) = {result}, Expected = {expected}, Match: {result == expected}")

if __name__ == "__main__":
    test_fibonacci()
    test_tribonacci()
    test_linear_recurrence()
