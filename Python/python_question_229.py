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
    Groups a list of strings into sublists where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups. Key: sorted string, Value: list of anagrams.

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group.
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group.

    return list(anagram_groups.values())  # Return the list of anagram groups.

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'eat', 'tea'], ['tan', 'nat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['ate', 'eat', 'tea'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['abc', 'cab', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['cab', 'abc', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['abc', 'cab', 'bca'], ['zyx', 'xyz']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['cab', 'abc', 'bca'], ['zyx', 'xyz']] or group_anagrams(["abc", "cab", "bca", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['zyx', 'xyz']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()