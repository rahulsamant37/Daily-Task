from collections import Counter
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        hmap = Counter(arr)
        if len(hmap)>=3:
            print("NO")
        else:
            freq1 = hmap[min(hmap)]
            freq2 = hmap[max(hmap)]
            if freq1 == freq2 or (n % 2 == 1 and abs(freq1 - freq2) == 1):
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()