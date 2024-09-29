# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

# Solution
def group_anagrams(strs):
    """
    Groups anagrams from a list of strings together.

    Args:
      strs: A list of strings.

    Returns:
      A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of original strings
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the original string to the existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group with the original string
    return list(anagram_groups.values())  # Return the values of the dictionary (list of lists)


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']] # order doesn't matter
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["", ""]) == [["", ""]]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['silent', 'listen', 'enlist']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'silent', 'listen']] or group_anagrams(["listen", "silent", "enlist"]) == [['enlist', 'listen', 'silent']] or group_anagrams(["listen", "silent", "enlist"]) == [['silent', 'enlist', 'listen']] or group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'enlist', 'silent']] # order doesn't matter
    assert group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'bca', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['bca', 'abc', 'cab'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['cab', 'bca', 'abc'], ['zyx', 'xyz']] # order doesn't matter
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()