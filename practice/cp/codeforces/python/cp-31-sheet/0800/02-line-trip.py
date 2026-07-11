def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        stations = list(map(int, input().split()))
        
        points = [0] + stations
        points.sort()
        
        max_gap = max(points[i+1]-points[i] for i in range(len(points)-1))
        last_gap = x - points[-1]
        max_gap = max(max_gap, last_gap*2)
        print(max_gap)

if __name__ == "__main__":
    solve()