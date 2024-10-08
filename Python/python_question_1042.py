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
    anagram_groups = {}  # Dictionary to store anagram groups, key is the sorted string
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group

    return list(anagram_groups.values())  # Return the values (lists of anagrams)
    

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['tea', 'eat', 'ate']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['ate', 'eat', 'tea']] or group_anagrams(["tan", "nat", "ate", "eat", "tea", "bat"]) == [['tan', 'nat'], ['ate', 'eat', 'tea'], ['bat']] or group_anagrams(["tan", "nat", "ate", "eat", "tea", "bat"]) == [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] or group_anagrams(["tan", "nat", "ate", "eat", "tea", "bat"]) == [['tan', 'nat'], ['ate', 'eat', 'tea'], ['bat']]

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", "a"]) == [["a"], ["a"]]

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()