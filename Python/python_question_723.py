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
    Groups a list of strings into sublists based on whether the strings are anagrams of each other.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, keyed by sorted string
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group for the anagram
    return list(anagram_groups.values())  # Return the values of the dictionary (lists of anagrams)


# Test cases
def test_group_anagrams():
    """
    Tests the group_anagrams function with several test cases.
    """
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", ""]) == [['a'], ['']]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['oof', 'foo']]
    print("All test cases passed!")


if __name__ == "__main__":
    test_group_anagrams()