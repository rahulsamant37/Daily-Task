# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. You can return the answer in any order.

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
    Groups a list of strings into sublists of anagrams.

    Args:
      strs: A list of strings.

    Returns:
      A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams.

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams.

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If sorted string exists, add the string to the existing list.
        else:
            anagram_groups[sorted_s] = [s]  # If sorted string doesn't exist, create a new list with the string.

    return list(anagram_groups.values())  # Return the values of the dictionary (lists of anagrams).


# Test cases
def test_solution():
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert group_anagrams(strs1) == [sorted(x) for x in expected1] or group_anagrams(strs1) == [sorted(x, reverse=True) for x in expected1] or group_anagrams(strs1) == expected1

    strs2 = [""]
    expected2 = [[""]]
    assert group_anagrams(strs2) == expected2

    strs3 = ["a"]
    expected3 = [["a"]]
    assert group_anagrams(strs3) == expected3

    strs4 = ["listen", "silent", "enlist"]
    expected4 = [["listen", "silent", "enlist"]]
    assert group_anagrams(strs4) == expected4 or group_anagrams(strs4) == [["enlist", "listen", "silent"]] or group_anagrams(strs4) == [["silent", "listen", "enlist"]]

    strs5 = ["abc", "bac", "cab", "xyz", "zyx"]
    expected5 = [["abc", "bac", "cab"], ["xyz", "zyx"]]
    assert group_anagrams(strs5) == [sorted(x) for x in expected5] or group_anagrams(strs5) == [sorted(x, reverse=True) for x in expected5] or group_anagrams(strs5) == expected5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()