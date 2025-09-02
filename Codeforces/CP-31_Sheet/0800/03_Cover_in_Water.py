def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        contiguous_three_dot = False
        total_dots = 0
        for i in range(n):
            if s[i]=="." and i+2<n and s[i+1]=="." and s[i+2]==".":
                contiguous_three_dot = True
                break
            if s[i] == ".":
                total_dots+=1
        if contiguous_three_dot:
            print(2)
        else:
            print(total_dots)

if __name__ == "__main__":
    solve()