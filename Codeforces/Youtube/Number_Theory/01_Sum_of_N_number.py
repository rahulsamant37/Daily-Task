import time

# O(N)
def sum_upto_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# O(1)
def sum_upto_n_optimized(n):
    return (n * (n + 1)) // 2

def solve():
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        
        print("-----## Normal ##--------")
        start = time.time()
        print("Sum:", sum_upto_n(n))
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")

        print("-----## Optimized ##--------")
        start = time.time()
        print("Sum:", sum_upto_n_optimized(n))
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        print()

if __name__ == "__main__":
    solve()
