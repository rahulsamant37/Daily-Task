# Python Question: Find the Largest Continuous Range in an Array
'''
Given an array of integers, find the largest (longest) range of consecutive integers within the array.  The range can contain numbers in any order.  Return the start and end of the range as a list.  If multiple ranges have the same largest length, return the first one encountered.

Example:
Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7]

Explanation:
The longest range of consecutive integers is [0, 1, 2, 3, 4, 5, 6, 7]. Therefore, the output should be [0, 7]. Note that the numbers in the input array are not necessarily sorted.
'''

# Solution
def solution():
    def largest_range(array):
        """
        Finds the largest range of consecutive integers in an array.

        Args:
            array: A list of integers.

        Returns:
            A list containing the start and end of the largest range.
        """

        nums = {}  # Use a dictionary to keep track of visited numbers
        for num in array:
            nums[num] = True  # Initially, mark all numbers as unvisited

        longest_range = []
        longest_length = 0

        for num in array:
            if not nums[num]:
                continue  # Skip if already visited

            nums[num] = False  # Mark as visited
            current_length = 1
            left = num - 1
            right = num + 1

            # Expand to the left
            while left in nums:
                if not nums[left]:
                    break # Already visited
                nums[left] = False  # Mark as visited
                current_length += 1
                left -= 1

            # Expand to the right
            while right in nums:
                if not nums[right]:
                    break # Already visited
                nums[right] = False  # Mark as visited
                current_length += 1
                right += 1

            # Update the longest range if necessary
            if current_length > longest_length:
                longest_length = current_length
                longest_range = [left + 1, right - 1]

        return longest_range
    return largest_range

# Test cases
def test_solution():
    def largest_range(array):
        """
        Finds the largest range of consecutive integers in an array.

        Args:
            array: A list of integers.

        Returns:
            A list containing the start and end of the largest range.
        """

        nums = {}  # Use a dictionary to keep track of visited numbers
        for num in array:
            nums[num] = True  # Initially, mark all numbers as unvisited

        longest_range = []
        longest_length = 0

        for num in array:
            if not nums[num]:
                continue  # Skip if already visited

            nums[num] = False  # Mark as visited
            current_length = 1
            left = num - 1
            right = num + 1

            # Expand to the left
            while left in nums:
                if not nums[left]:
                    break # Already visited
                nums[left] = False  # Mark as visited
                current_length += 1
                left -= 1

            # Expand to the right
            while right in nums:
                if not nums[right]:
                    break # Already visited
                nums[right] = False  # Mark as visited
                current_length += 1
                right += 1

            # Update the longest range if necessary
            if current_length > longest_length:
                longest_length = current_length
                longest_range = [left + 1, right - 1]

        return longest_range

    assert largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]) == [0, 7]
    assert largest_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10]
    assert largest_range([10, 11, 12]) == [10, 12]
    assert largest_range([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]) == [10, 19]
    assert largest_range([4, 2, 1, 3]) == [1, 4]
    assert largest_range([8, 4, 2, 10, 3, 6, 7, 9, 1]) == [6, 10]
    assert largest_range([0, -5, 9, 2, 8, 1, 3, -4, 7, -3, 6, 5]) == [-5, 9]
    assert largest_range([1, 2, 3, 4, 5]) == [1, 5]
    assert largest_range([5, 4, 3, 2, 1]) == [1, 5]
    assert largest_range([1]) == [1, 1]
    assert largest_range([]) == []
    assert largest_range([4, 4, 5, 6]) == [4, 6]
    assert largest_range([1, 2, 0, 1, 3]) == [0, 3]

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()