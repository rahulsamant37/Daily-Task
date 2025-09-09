def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n==2 or n==3:
        print("NO SOLUTION")
    else:
        even = list(range(2, n+1, 2))
        odd = list(range(1, n+1, 2))
        result = even + odd
        print(" ".join(map(str,result)))

if __name__ == "__main__":
    solve()