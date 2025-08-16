# Python Question: Group Anagrams
'''
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

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
    Groups anagrams together in a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams. Key: sorted string, Value: list of anagrams
    
    for s in strs:
        sorted_s = "".join(sorted(s)) # Sort the string to create a unique key for anagrams
        
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s) # Add the string to the corresponding anagram group
        else:
            anagram_groups[sorted_s] = [s] # Create a new anagram group for this sorted string
    
    return list(anagram_groups.values()) # Return the list of anagram groups

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['nat', 'tan']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['nat', 'tan']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['nat', 'tan']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]
    assert group_anagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]) == [['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()