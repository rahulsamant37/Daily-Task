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
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string (canonical form)
    for s in strs:
        # Create a canonical form of the string by sorting its characters
        sorted_s = "".join(sorted(s))
        # If the canonical form is already a key in the dictionary, append the string to the existing group
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new group with the canonical form as the key and the string as the first element
        else:
            anagram_groups[sorted_s] = [s]
    # Return the values of the dictionary (which are the lists of anagrams)
    return list(anagram_groups.values())


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['ate', 'eat', 'tea'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]
    assert group_anagrams(["abc","cba","bac","foo","oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc","cba","bac","foo","oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc","cba","bac","foo","oof"]) == [['bac', 'abc', 'cba'], ['foo', 'oof']] or group_anagrams(["abc","cba","bac","foo","oof"]) == [['foo', 'oof'], ['abc', 'cba', 'bac']] or group_anagrams(["abc","cba","bac","foo","oof"]) == [['foo', 'oof'], ['cba', 'abc', 'bac']] or group_anagrams(["abc","cba","bac","foo","oof"]) == [['foo', 'oof'], ['bac', 'abc', 'cba']]

if __name__ == "__main__":
    test_group_anagrams()