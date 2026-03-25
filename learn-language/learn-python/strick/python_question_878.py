# Python Question: Group Anagrams
'''
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups anagrams together in a list of strings.

    Args:
      strs: A list of strings.

    Returns:
      A list of lists, where each inner list contains anagrams.
    """
    # Create a dictionary to store anagrams, where the key is the sorted string and the value is a list of anagrams.
    anagram_groups = {}

    # Iterate through the input list of strings.
    for s in strs:
        # Sort the string to create a unique key for anagrams.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the current string to the corresponding list.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the current string as the value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    # Test case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result1 = group_anagrams(strs1)
    assert sorted([sorted(x) for x in result1]) == sorted([sorted(x) for x in expected1]), f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test case 2
    strs2 = [""]
    expected2 = [[""]]
    result2 = group_anagrams(strs2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test case 3
    strs3 = ["a"]
    expected3 = [["a"]]
    result3 = group_anagrams(strs3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    # Test case 4
    strs4 = ["listen", "silent", "enlist"]
    expected4 = [["listen", "silent", "enlist"]]
    result4 = group_anagrams(strs4)
    assert sorted([sorted(x) for x in result4]) == sorted([sorted(x) for x in expected4]), f"Test Case 4 Failed: Expected {expected4}, got {result4}"

    # Test case 5 (empty list)
    strs5 = []
    expected5 = []
    result5 = group_anagrams(strs5)
    assert result5 == [], f"Test Case 5 Failed: Expected {expected5}, got {result5}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()