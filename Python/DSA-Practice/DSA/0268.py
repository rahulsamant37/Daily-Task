# DSA Problem 268

'''
Problem Statement:
You are given a list of numbers and a target sum. Your task is to find all unique combinations of numbers that add up to the target sum. Each number in the list can be used unlimited times, and the same combination in a different order is considered the same combination. Return a list of all unique combinations that add up to the target sum.

For example, given the list [2, 3, 6, 7] and the target sum of 7, the solution would be [[2, 2, 3], [7]], as these are the only unique combinations that sum up to 7.
'''

Solution:
def combination_sum(candidates, target):
    def backtrack(remaining, combination, start, result):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # add the number into the combination
            combination.append(candidates[i])
            # give the function a new remain value
            backtrack(remaining - candidates[i], combination, i, result)
            # remove the number from the combination
            combination.pop()
    
    candidates.sort()
    result = []
    backtrack(target, [], 0, result)
    return result

# Test the function
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  # Output: [[2, 2, 3], [7]]