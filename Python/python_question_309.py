# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups a list of strings into sublists of anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is the list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key for anagram grouping
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If the sorted string is already a key, append the current string to the list
        else:
            anagram_groups[sorted_s] = [s]  # If the sorted string is not a key, create a new list with the current string
    return list(anagram_groups.values())  # Return the list of lists of anagrams

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["", ""]) == [["", ""]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'bca', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'bca', 'cba']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()