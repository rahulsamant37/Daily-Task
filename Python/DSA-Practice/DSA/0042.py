# DSA Problem 42

'''
Problem Statement:
A sequence of positive integers, `nums`, is given. A move consists of choosing two adjacent integers in `nums` and replacing them with their sum. The cost of this move is the sum of the two integers. The goal is to reduce the array to a single integer. Find the minimum possible total cost of all moves.

Example:
Input: nums = [1, 2, 3, 4]
Output: 19
Explanation: One of the optimal sequences of moves:
- Combine 1 and 2 to get 3 (cost 3), nums becomes [3, 3, 4].
- Combine 3 and 3 to get 6 (cost 6), nums becomes [6, 4].
- Combine 6 and 4 to get 10 (cost 10), nums becomes [10].
Total cost = 3 + 6 + 10 = 19.
'''

Solution:
```python
def min_cost_to_combine(nums):
    from heapq import heapify, heappop, heappush
    
    # Convert the list into a min heap
    heapify(nums)
    
    total_cost = 0
    while len(nums) > 1:
        # Pop the two smallest numbers
        first = heappop(nums)
        second = heappop(nums)
        
        # Calculate the cost of combining them
        cost = first + second
        total_cost += cost
        
        # Push the combined number back into the heap
        heappush(nums, cost)
    
    return total_cost

# Check function to verify the correctness of the solution
def check_solution():
    assert min_cost_to_combine([1, 2, 3, 4]) == 19
    assert min_cost_to_combine([1, 10, 6, 2]) == 39
    assert min_cost_to_combine([5]) == 0  # Edge case: single element
    print("All tests passed!")

check_solution()
```

This problem and solution demonstrate an optimal approach to minimizing the total cost of combining numbers in an array, using a min heap to always combine the smallest available numbers, thus reducing the overall cost of the operation.