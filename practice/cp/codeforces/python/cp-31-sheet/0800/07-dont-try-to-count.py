def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input().strip()
        x = input().strip()

        current = s
        if x in current:
            print(0)
            continue

        found = False
        for i in range(1, 6):
            current = current + current
            if x in current:
                print(i)
                found = True
                break
        if not found:
            print(-1)

solve()