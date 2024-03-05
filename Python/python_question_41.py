# Python Question: Find the largest number that can be divided by each of the numbers from 2 to 10 without any remainder

def findLargestDivisibleNumber(nums):
    '''
    Given a list of positive numbers, find the largest number that can be divided by each of the numbers from 2 to the given list without any remainder.

    Example:
    Input: nums = [12, 24, 36, 48, 60]
    Output: 96 (60 is the largest number that can be divided by 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 36, 40, 45, 50, 60 without any remainder)
    '''
    product = nums[0]
    largest_number = nums[0]
    for num in nums[1:]:
        while product % num == 0:
            product /= num
        largest_number = max(largest_number, product)
    return largest_number

def main():
    nums = [12, 24, 36, 48, 60]
    print("The largest number is", findLargestDivisibleNumber(nums))

if __name__ == "__main__":
    main()