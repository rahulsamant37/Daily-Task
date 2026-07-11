# Python Question: Search an element in a sorted array of integers
'''
Given a sorted integer array of size n, search a target element.

Example:

Input: array = [1, 3, 5, 7, 11]
target = 7
Output: 7 is present at index 3

Input: array = [1, 3, 5, 7, 11]
target = 9
Output: 9 is not present in the array
'''

# Solution
def search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    array = [1, 3, 5, 7, 11]
    target = 7
    index = search(array, target)

    if index != -1:
        print(f"{target} is present at index {index}")
    else:
        print(f"{target} is not present in the array")