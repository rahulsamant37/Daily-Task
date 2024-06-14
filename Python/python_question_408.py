# Python Question: Find the Longest Increasing Subsequence
'''
Given an array of integers, find the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

# Solution
def solution():
    def longest_increasing_subsequence(nums):
        """
        Finds the length of the longest increasing subsequence in a given array.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest increasing subsequence.
        """
        if not nums:
            return 0

        # tails[i] is the smallest tail of all increasing subsequences with length i+1.
        tails = []

        # Iterate through the input array.
        for num in nums:
            # If we find a tail that is greater than or equal to the current number,
            # we can replace that tail with the current number, because it creates a
            # new increasing subsequence of the same length, but with a smaller tail.
            # This is done using binary search for efficiency.
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1

            # If we didn't find a tail that is greater than or equal to the current number,
            # it means the current number is greater than all tails, so we can extend the
            # longest increasing subsequence by one.
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num

        # The length of the tails array is the length of the longest increasing subsequence.
        return len(tails)

    return longest_increasing_subsequence

# Test cases
def test_solution():
    nums1 = [10,9,2,5,3,7,101,18]
    assert solution()(nums1) == 4

    nums2 = [0,1,0,3,2,3]
    assert solution()(nums2) == 4

    nums3 = [7,7,7,7,7,7,7]
    assert solution()(nums3) == 1

    nums4 = [1,3,6,7,9,4,10,5,6]
    assert solution()(nums4) == 6

    nums5 = []
    assert solution()(nums5) == 0

    nums6 = [1]
    assert solution()(nums6) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()