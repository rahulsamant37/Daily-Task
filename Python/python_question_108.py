# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''

# Solution
def solution():
    def group_anagrams(strs):
        """
        Groups a list of strings into sublists of anagrams.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each sublist contains anagrams.
        """

        anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams

        for s in strs:
            sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s].append(s)  # If the key exists, append the string to the list
            else:
                anagram_groups[sorted_s] = [s]  # If the key doesn't exist, create a new list with the string

        return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list

    return group_anagrams # returning the function to be tested in test_solution

# Test cases
def test_solution():
    def test_group_anagrams():
        group_anagrams = solution()
        # Test case 1
        input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        actual1 = group_anagrams(input1)
        # Sort each sublist to make comparison easier, as order doesn't matter
        for sublist in actual1:
            sublist.sort()
        for sublist in expected1:
            sublist.sort()

        # Sort the list of sublists by length to ensure consistent comparison order
        actual1.sort(key=len)
        expected1.sort(key=len)

        assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, but got {actual1}"

        # Test case 2
        input2 = [""]
        expected2 = [[""]]
        actual2 = group_anagrams(input2)

        for sublist in actual2:
            sublist.sort()
        for sublist in expected2:
            sublist.sort()
        actual2.sort(key=len)
        expected2.sort(key=len)

        assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, but got {actual2}"

        # Test case 3
        input3 = ["a"]
        expected3 = [["a"]]
        actual3 = group_anagrams(input3)

        for sublist in actual3:
            sublist.sort()
        for sublist in expected3:
            sublist.sort()
        actual3.sort(key=len)
        expected3.sort(key=len)

        assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, but got {actual3}"

        # Test case 4
        input4 = ["listen", "silent", "enlist", "tinsel"]
        expected4 = [["listen", "silent", "enlist"], ["tinsel"]]
        actual4 = group_anagrams(input4)

        for sublist in actual4:
            sublist.sort()
        for sublist in expected4:
            sublist.sort()
        actual4.sort(key=len)
        expected4.sort(key=len)

        assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, but got {actual4}"

        # Test case 5 (empty list)
        input5 = []
        expected5 = []
        actual5 = group_anagrams(input5)

        assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, but got {actual5}"

        print("All test cases passed!")

    test_group_anagrams()

if __name__ == "__main__":
    test_solution()