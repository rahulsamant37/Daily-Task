
## 1. Intersection Of Two Arrays
def intersection_of_arrays(arr1, arr2):
    intersected = {}
    result = []

    for num in arr1:
        intersected[num] = True

    for i in arr2:
        if i in intersected and i not in result:
            result.append(i)
    return result

# Example Usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2,1]
print(intersection_of_arrays(arr1, arr2))


# 2. Check for Duplicates

def contains_duplicates(nums): 
    duplicate = {}
    
    for num in nums:
        if num in duplicate.keys():
            duplicate[num]+=1
        else:
            duplicate[num]=1
    return [k for k,v in duplicate.items() if v>=2]

# Example Usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(contains_duplicates(nums1))  # Output: True
print(contains_duplicates(nums2))  # Output: False


# 3. First None Repeating Character in a string

def first_non_repeating_char(s):
    fnr = {}

    for i in s:
        if i in fnr:
            fnr[i]+=1
        else:
            fnr[i]=1
    return [k for k,v in fnr.items() if v==1][0]


# Example Usage:
s = "swiss"
print(first_non_repeating_char(s)) # 'w'


