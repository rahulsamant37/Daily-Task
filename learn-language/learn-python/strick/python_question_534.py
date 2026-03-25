# Python Question: Minimum Jumps to Reach End
'''
You are given an array of non-negative integers `nums`. You are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you can reach the last index. If you can, return the minimum number of jumps required to reach the last index. If you cannot reach the last index, return -1.

Example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2

Input: nums = [0]
Output: 0

Input: nums = [1,0]
Output: 1

Input: nums = [1,1,1,1]
Output: 3

Input: nums = [3,2,1,0,4]
Output: -1
'''

# Solution
def solution():
    def jump(nums):
        """
        Calculates the minimum number of jumps to reach the last index of an array.

        Args:
            nums: A list of non-negative integers representing the maximum jump length at each position.

        Returns:
            The minimum number of jumps required to reach the last index, or -1 if it's not reachable.
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_reach = 0  # The farthest index we can reach with the current number of jumps
        max_reach = 0      # The farthest index we can reach from the current position

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i]) # Update the farthest reachable position

            if i == current_reach: # If we've reached the limit of our current jump
                jumps += 1         # Make another jump
                if current_reach >= max_reach: # Check if we're stuck (can't reach further)
                    return -1
                current_reach = max_reach     # Update the farthest reachable position after the jump

                if current_reach >= n - 1:
                    return jumps

        return jumps if max_reach >= n - 1 else -1

    return jump

# Test cases
def test_solution():
    jump = solution()

    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2
    assert jump([0]) == 0
    assert jump([1,0]) == 1
    assert jump([1,1,1,1]) == 3
    assert jump([3,2,1,0,4]) == -1
    assert jump([5,9,3,2,1,0,2,3,3,1,0,0]) == 2
    assert jump([1,2,3]) == 2
    assert jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,3,5,6,6,5,8,2,6,3,0,0,0,0,0,0,0,0,0,0,0]) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()