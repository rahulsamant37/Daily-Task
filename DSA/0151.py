# DSA Problem 151

'''
Problem Statement:
Given a list of non-negative integers `nums`, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return -1.

For example, given nums = [2, 3, 1, 1, 4], the minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

Solution:
```python
def minJumps(nums):
    n = len(nums)
    if n <= 1:
        return 0
    
    # If the first element is zero, then we cannot move forward
    if nums[0] == 0:
        return -1
    
    # The number of steps we can take from the current position
    steps = nums[0]
    # The maximum reach from the current position
    maxReach = nums[0]
    # The number of jumps necessary to reach that maximum reach
    jumps = 1
    
    for i in range(1, n):
        # If we have reached the maximum reach with the current number of jumps
        if i == n - 1:
            return jumps
        
        # Updating the maximum reach
        maxReach = max(maxReach, i + nums[i])
        
        # We have used a jump
        steps -= 1
        
        # If no more steps are remaining
        if steps == 0:
            # We must have used a jump
            jumps += 1
            
            # Check if the current index / position is reachable
            if i >= maxReach:
                return -1
            
            # Re-initialize the steps to the amount of steps to reach maxReach from position i
            steps = maxReach - i
    
    return -1

# Example usage:
nums = [2, 3, 1, 1, 4]
print(minJumps(nums))  # Output: 2
```

This solution iterates through the array while maintaining the maximum distance it can reach (`maxReach`) and the steps remaining from the current jump (`steps`). It increments the jump count when it exhausts the current jump's reach and updates the maximum reach whenever a new position is reached.