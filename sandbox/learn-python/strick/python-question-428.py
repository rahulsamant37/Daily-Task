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
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string (tuple), value is a list of anagrams
    
    for s in strs:
        # Sort the string to create a unique key for anagrams.  Using tuple as key since lists are mutable and cannot be keys
        sorted_s = tuple(sorted(s))
        
        # If the sorted string is already a key in the dictionary, add the current string to the corresponding list.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the current string as the value.
        else:
            anagram_groups[sorted_s] = [s]
    
    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", "a"]) == [['a'], ['a']]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['oof', 'foo']]

if __name__ == "__main__":
    test_group_anagrams()