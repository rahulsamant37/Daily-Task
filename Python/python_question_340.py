# Python Question: Group Anagrams
'''
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups anagrams together in a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups (key: sorted string, value: list of anagrams)

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If the key exists, append the string to the list
        else:
            anagram_groups[sorted_s] = [s]  # If the key doesn't exist, create a new list with the string

    return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", ""]) == [['a'], ['']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['silent', 'listen', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'silent', 'listen']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'listen', 'silent']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()