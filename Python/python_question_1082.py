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
    Groups anagrams together from a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group with the string

    return list(anagram_groups.values())  # Return the values of the dictionary (lists of anagrams)


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'ate', 'eat'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", "a"]) == [['a'], ['a']] or group_anagrams(["a", "a"]) == [['a', 'a']]
    assert group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'cab', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'abc', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'cab', 'abc'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'abc', 'bca'], ['zyx', 'xyz']]

if __name__ == "__main__":
    test_group_anagrams()