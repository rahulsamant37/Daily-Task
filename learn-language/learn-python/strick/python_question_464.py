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
        A list of lists, where each sublist contains anagrams.
    """

    # Create a dictionary to store the anagrams. The key is the sorted string,
    # and the value is a list of strings that are anagrams of each other.
    anagram_groups = {}

    # Iterate over the input list of strings.
    for string in strs:
        # Sort the string to create a unique key for anagrams.
        sorted_string = "".join(sorted(string))

        # If the sorted string is already a key in the dictionary,
        # add the current string to the corresponding list.
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(string)
        # Otherwise, create a new entry in the dictionary with the sorted string
        # as the key and a list containing the current string as the value.
        else:
            anagram_groups[sorted_string] = [string]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_solution():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['bat'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'bca', 'cba']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'listen', 'silent']] or group_anagrams(["listen", "silent", "enlist"]) == [['silent', 'enlist', 'listen']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()