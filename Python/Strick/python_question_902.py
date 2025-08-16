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
    anagram_groups = {}  # Dictionary to store anagram groups, key is sorted string, value is list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group
    return list(anagram_groups.values())  # Return the list of anagram groups

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'abc', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'bca', 'abc'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'cba', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'abc', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'cba', 'abc'], ['xyz', 'zyx']]
    assert group_anagrams(["aabb", "abab", "bbaa"]) == [['aabb', 'abab', 'bbaa']] or group_anagrams(["aabb", "abab", "bbaa"]) == [['abab', 'aabb', 'bbaa']] or group_anagrams(["aabb", "abab", "bbaa"]) == [['bbaa', 'abab', 'aabb']] or group_anagrams(["aabb", "abab", "bbaa"]) == [['aabb', 'bbaa', 'abab']] or group_anagrams(["aabb", "abab", "bbaa"]) == [['bbaa', 'aabb', 'abab']] or group_anagrams(["aabb", "abab", "bbaa"]) == [['abab', 'bbaa', 'aabb']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()