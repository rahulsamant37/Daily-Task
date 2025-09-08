def solve():
    s = str(input())
    max_len = 0
    length = 1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            length+=1
        else:
            max_len = max(max_len, length)
            length = 1
    max_len = max(max_len, length)
    print(max_len)

if __name__ == "__main__":
    solve()