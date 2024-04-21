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
    Groups a list of strings into sublists based on whether they are anagrams of each other.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups, key is sorted string, value is list of anagrams
    
    for str_val in strs:
        # Sort the string to use it as a key in the dictionary
        sorted_str = "".join(sorted(str_val))
        
        # If the sorted string is already a key, append the current string to the list
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(str_val)
        else:
            # Otherwise, create a new list with the current string as the first element
            anagram_groups[sorted_str] = [str_val]
    
    # Return the values of the dictionary as a list of lists
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", ""]) == [['a'], ['']] or group_anagrams(["a", ""]) == [[''], ['a']]
    assert group_anagrams(["abc", "bac", "cab", "xyz", "zyx"]) == [['abc', 'bac', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bac", "cab", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'bac', 'cab']]

if __name__ == "__main__":
    test_group_anagrams()