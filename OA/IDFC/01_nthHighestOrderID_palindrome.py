# brute-force version
## O(N⋅logM), O(logM)
def nthHighestOrderID(M, N):
    res = 0
    count = 0
    num = M + 1   # start checking numbers greater than M

    while True:
        if str(num) == str(num)[::-1]:  # check palindrome
            count += 1
            if count == N:  # found Nth palindrome
                res = num
                break
        num += 1
    return res

# This optimized version is significantly faster than the brute-force version, especially when M is large 
# because it skips non-palindromic numbers altogether.
## O(N) (worst case), O(log M), 
def nthHighestOrderID_Optimized(M, N):
    res = 0
    found = 0
    
    # We only need palindromes up to ~10 digits since M < 2^31
    # Generate by mirroring half numbers
    length = 1
    while True:
        half_len = (length + 1) // 2
        start = 10**(half_len - 1) if half_len > 1 else 1
        end = 10**half_len
        
        for half in range(start, end):
            s = str(half)
            if length % 2 == 0:
                pal = int(s + s[::-1])
            else:
                pal = int(s + s[-2::-1])
            
            if pal > M:
                found += 1
                if found == N:
                    return pal
        length += 1


def main():
    S = input().split()
    M = int(S[0])
    N = int(S[1])
    print(nthHighestOrderID(M, N))
    print(nthHighestOrderID_Optimized(M, N))

main()
