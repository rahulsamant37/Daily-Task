# DSA Problem 214

'''
Problem Statement:
You are given a list of positive integers, `nums`, and an integer `k`. You are allowed to perform the following operation any number of times: choose any element from `nums` and increase it by `k`. Your goal is to make all elements in the list equal. However, each operation has a cost equal to the value of the element after the increment. For example, incrementing a number `x` to `x + k` costs `x + k`. Find the minimum cost to make all elements equal.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= k <= 10^4

Input:
The first line contains two space-separated integers, `n` and `k`, where `n` is the number of elements in the list `nums`, and `k` is the increment value.
The second line contains `n` space-separated integers representing the elements of the list `nums`.

Output:
Print a single integer representing the minimum cost to make all elements equal.

Example:
Input:
5 3
1 2 3 4 5
Output:
21
Explanation:
We can increment the elements to make them all equal to 9 with a total cost of 21.
'''

Solution:
def min_cost_to_equal_elements(n, k, nums):
    nums.sort()
    target = nums[(n - 1) // 2]
    cost = 0
    for num in nums:
        diff = (target - num + k - 1) // k * k
        cost += diff + num
    return cost

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(min_cost_to_equal_elements(n, k, nums))

# This solution calculates the minimum cost to make all elements in the list equal by incrementing them by `k`.
# The median is used as the target value to minimize the total cost, and the cost is computed based on the difference
# from the target value for each element.