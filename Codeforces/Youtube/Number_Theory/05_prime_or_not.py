## O(root n), O(1), Efficient and clean for large n
def is_prime_6k(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
            return True
        i+=6
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_prime_6k(n))