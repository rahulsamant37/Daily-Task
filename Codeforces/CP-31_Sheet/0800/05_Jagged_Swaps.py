def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if arr[0]!=1:
            print("NO")
        else:
            print("YES")
if __name__ == "__main__":
    solve()
