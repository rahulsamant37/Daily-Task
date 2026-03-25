# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder
'''
Find the largest number that can be divided by each number from 2 to 10 without any remainder.

Example:
Input: list(range(2, 11))  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 52 (as 52 is the largest number which leaves a remainder of 0 when divided by 2, 3, 4, 5, 6, 7, 8, 9, and 10)
'''

def find_largest_divisible_number(nums):
    # Initialize the largest number
    largest_number = nums[0]
    
    # Iterate from 2 to n (where n is the length of nums)
    for i in range(2, len(nums)):
        # Check if nums[i] divides nums[0] without any remainder
        if nums[i] % nums[0] == 0:
            # Update the largest number if nums[i] is greater than largest_number
            if nums[i] > largest_number:
                largest_number = nums[i]
    
    return largest_number

if __name__ == "__main__":
    nums = list(range(2, 11))
    print("The largest number that can be divided by each number from 2 to 10 without any remainder is", find_largest_divisible_number(nums))