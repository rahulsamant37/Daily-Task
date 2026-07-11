# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Given a range of numbers from 2 to 10, find the largest number that can be divided by each number from the range without any remainder.

For example, consider the numbers 2 to 10. The largest number that satisfies the condition is 10. It is divisible by 2, 3, 4, 5, 6, 7, 8, and 9 without any remainder.
'''

def largest_common_divisor(nums):
    '''
    Function to find the largest number that satisfies the given condition.
    
    Parameters:
    nums (list): List of numbers from 2 to 10
    
    Returns:
    int: Largest number that satisfies the condition
    '''
    # Initialize the result
    result = nums[0]

    # Iterate through the list and find the largest number
    for num in nums:
        while num > 1:
            if num % result == 0:
                result = num
            num //= 2

    return result

if __name__ == "__main__":
    nums = [2, 3, 4, 5, 6, 7, 8, 9]
    print("The largest number that satisfies the condition is", largest_common_divisor(nums))