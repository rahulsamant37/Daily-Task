## Optimal Approach
class Solution:
    def maxSubArray(self, nums):
        maxSum = float('-inf') ## The expression float('-inf') in Python represents negative infinity.
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum

## Brute Force
class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
result = solution.maxSubArray(nums)
print(result)