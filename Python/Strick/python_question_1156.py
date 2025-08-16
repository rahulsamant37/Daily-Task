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
    Groups a list of strings into sublists based on whether they are anagrams of each other.

    Args:
      strs: A list of strings.

    Returns:
      A list of lists, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group

    return list(anagram_groups.values())  # Return the list of anagram groups

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["", ""]) == [["", ""]]
    assert group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'bca', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'bca', 'abc'], ['zyx', 'xyz']]

if __name__ == "__main__":
    test_group_anagrams()