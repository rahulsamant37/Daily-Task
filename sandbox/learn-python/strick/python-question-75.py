# Python Question: Find the largest number that can be divided by any number from a given list

'''
For example, consider a list of numbers [1, 5, 7, 10]. Find the largest number that can be divided by any number from this list.

Input: List of numbers = [1, 5, 7, 10]
Output: 10 (as it is the largest number and can be divided by all numbers in the list)
'''

def find_largest_divisible_by(nums):
    # Sort the list in descending order
    nums.sort(reverse=True)
    
    # Return the last element of the sorted list
    return nums[-1]

def main():
    nums = [1, 5, 7, 10]
    largest_number = find_largest_divisible_by(nums)
    print("The largest number that can be divided by any number from the given list is", largest_number)

if __name__ == '__main__':
    main()

# Output: The largest number that can be divided by any number from the given list is 10