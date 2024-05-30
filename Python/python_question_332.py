# Python Question: Minimum Jumps to Reach End
'''
You are given an array of non-negative integers called `nums`. You are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.

For example:
Input: nums = [2,3,1,1,4]
Output: True
Explanation: Jump 2 steps from index 0 to 2, then jump 2 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: False
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

# Solution
def solution():
    def can_jump(nums):
        """
        Determines if it's possible to reach the end of the array given the jump lengths.

        Args:
            nums: A list of non-negative integers representing jump lengths.

        Returns:
            True if it's possible to reach the end, False otherwise.
        """
        n = len(nums)
        reachable = 0  # Initialize the farthest reachable index

        for i in range(n):
            # If the current index is beyond the reachable index, we cannot reach the end
            if i > reachable:
                return False

            # Update the farthest reachable index
            reachable = max(reachable, i + nums[i])

            # If we can reach the end from the current index, we are done
            if reachable >= n - 1:
                return True

        return reachable >= n - 1  # Double check that we reached the end

    return can_jump
    

# Test cases
def test_solution():
    can_jump = solution()
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False
    assert can_jump([0]) == True
    assert can_jump([2,0,0]) == True
    assert can_jump([1,0,1,0]) == False
    assert can_jump([5,9,3,2,1,0,2,3,3,1,0,0]) == True
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()