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
    Groups a list of strings into sublists where each sublist contains anagrams of each other.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Use a dictionary to store anagram groups
    
    for s in strs:
        # Sort the characters in the string to create a unique key for anagrams
        sorted_string = "".join(sorted(s))
        
        # If the sorted string is already a key in the dictionary, append the original string to the list
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the original string as the value
        else:
            anagram_groups[sorted_string] = [s]
    
    # Return the values of the dictionary as a list of lists
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']] # Order does not matter
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'bca', 'cba']]# Order does not matter
    assert group_anagrams(["listen", "silent", "enlist", "tinsel"]) == [['listen', 'silent', 'enlist'], ['tinsel']] or group_anagrams(["listen", "silent", "enlist", "tinsel"]) == [['tinsel'], ['listen', 'silent', 'enlist']]

if __name__ == "__main__":
    test_group_anagrams()