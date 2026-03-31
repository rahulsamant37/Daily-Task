def count_frequency(nums):
    ans = {}
    for eachNumber in nums:
        if eachNumber in ans:
            ans[eachNumber] += 1
        else:
            ans[eachNumber] = 1
    return ans

nums = [1,2,3,2,1,2,1,3,2,1,2,3]

result = count_frequency(nums)
print(result)