"""
1. Why do we go only up to √n?
- Every composite number (i.e. not prime) can be written as a product: a * b = n
- If both a and b were greater than sqrt(n), then their product would be greater than n, which is not allowed.
- So at least one of them must be ≤ sqrt(n)

2. Why start at i*i = 9 instead of 2*i = 6?
- Because numbers like 6 and 12 (which are 2×3, 2×6, etc.) have already been marked when i = 2.
- This saves time and keeps the algorithm efficient.
"""

def seive(n):
    isprime = [True]*(n+1)
    isprime[0:2] = [False, False]
    for i in range(2,int(n**0.5)+1):
        if isprime:
            for j in range(i*i,n+1,i):
                isprime[j]=False
    return isprime

print(seive(30))