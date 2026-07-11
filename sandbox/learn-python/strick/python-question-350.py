# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups a list of strings into sublists where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add to existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group

    return list(anagram_groups.values())  # Return the values (lists of anagrams)

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'ate', 'tea']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'ate', 'tea'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'ate', 'tea'], ['tan', 'nat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['abc', 'cab', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'cab', 'bca']]
    assert group_anagrams(["ddddddddddg","dgggggggggg"]) == [['ddddddddddg'], ['dgggggggggg']]

if __name__ == "__main__":
    test_group_anagrams()