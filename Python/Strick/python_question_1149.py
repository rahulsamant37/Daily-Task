# Python Question: Group Anagrams
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups anagrams in a list of strings together.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group for this anagram

    return list(anagram_groups.values())  # Return the values (lists of anagrams)

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'abc', 'cba'], ['foo', 'oof']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['silent', 'listen', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'silent', 'listen']]
    print("All test cases passed")

if __name__ == "__main__":
    test_group_anagrams()