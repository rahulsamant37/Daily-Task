def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count=0
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            count+=arr[i-1]-arr[i]
            arr[i]=arr[i-1]
    print(count)
if __name__ == "__main__":
    solve()