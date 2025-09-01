def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        if k == 1:
            if arr == sorted(arr):
                print("YES")
            else:
                print("NO")
        else:
            print("Yes")
if __name__ == "__main__":
    solve()