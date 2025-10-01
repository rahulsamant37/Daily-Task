"""
Problem: Two Sum
DESCRIPTION
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
"""

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        l, r = 0, n-1
        while l<r:
            t = arr[l]+arr[r]
            if t==k:
                return True
            elif t<k:
                l+=1
            else:
                r-=1
        return False

if __name__ == "__main__":
    print(solve())