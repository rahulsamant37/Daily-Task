# Python Question: Find the Longest Increasing Subsequence (LIS)
'''
Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS).
An increasing subsequence is a sequence of numbers from the array that are in strictly increasing order, but not necessarily consecutive.

Example:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums):
        """
        Finds the length of the longest increasing subsequence (LIS) in a given list of numbers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the LIS.
        """
        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        tails = []

        # Iterate through the numbers in the input list
        for num in nums:
            # If we find a number in 'tails' that is greater than or equal to the current number,
            # it means we can potentially replace that number with the current number to form a smaller tail for an increasing subsequence of the same length.
            # We use binary search to efficiently find the smallest number in 'tails' that is greater than or equal to the current number.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find any number in 'tails' that is greater than or equal to the current number,
            # it means the current number extends the longest increasing subsequence by 1.
            # In this case, we append the current number to 'tails'.
            if l == len(tails):
                tails.append(num)
            # Otherwise, we replace the number at index 'l' in 'tails' with the current number.
            # This is because the current number allows us to form an increasing subsequence of the same length, but with a smaller tail.
            else:
                tails[l] = num

        # The length of 'tails' is the length of the LIS.
        return len(tails)
    return longest_increasing_subsequence

# Test cases
def test_solution():
    lis = solution()
    assert lis([]) == 0
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis([0, 1, 0, 3, 2, 3]) == 4
    assert lis([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert lis([5,4,3,2,1]) == 1
    assert lis([1,3,6,7,9,4,10,5,6]) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()