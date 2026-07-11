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
    Groups a list of strings into sublists of anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add to existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group
    return list(anagram_groups.values())  # Return the values (lists of anagrams)

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['tea', 'eat', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['ate', 'eat', 'tea']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [["abc", "bca", "cba"], ["xyz", "zyx"]] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'cba', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'abc', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'cba', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'abc', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'bca', 'abc'], ['xyz', 'zyx']] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ["abc", "bca", "cba"]] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ['abc', 'cba', 'bca']] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ['bca', 'abc', 'cba']] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ['bca', 'cba', 'abc']] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ['cba', 'abc', 'bca']] or group_anagrams(["xyz", "zyx", "abc", "bca", "cba"]) == [["xyz", "zyx"], ['cba', 'bca', 'abc']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [["listen", "silent", "enlist"]] or group_anagrams(["listen", "silent", "enlist"]) == [["silent", "listen", "enlist"]] or group_anagrams(["listen", "silent", "enlist"]) == [["enlist", "silent", "listen"]] or group_anagrams(["listen", "silent", "enlist"]) == [["enlist", "listen", "silent"]] or group_anagrams(["listen", "silent", "enlist"]) == [["silent", "enlist", "listen"]] or group_anagrams(["listen", "silent", "enlist"]) == [["listen", "enlist", "silent"]]

if __name__ == "__main__":
    test_group_anagrams()