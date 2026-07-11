## O(root n), O(K), works upt to n ~ 10**12
def divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors) ## This step is upto us to implement or not depending upon use case