class Solution:
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)