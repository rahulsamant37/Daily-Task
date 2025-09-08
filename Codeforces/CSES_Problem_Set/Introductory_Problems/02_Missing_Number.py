def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    print(((n*(n+1))//2) - sum(arr))

if __name__ == "__main__":
    solve()