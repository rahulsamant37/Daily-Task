## Two Pointer
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

nums = [1,2,3,4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)