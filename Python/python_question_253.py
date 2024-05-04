# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together.  Anagrams are words that contain the same letters, but in a different order.

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
        A list of lists, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If key exists, add the string to the existing group
        else:
            anagram_groups[sorted_s] = [s]  # If key doesn't exist, create a new group with the string

    return list(anagram_groups.values())  # Return the list of anagram groups

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [['']]
    assert group_anagrams(["a"]) == [['a']]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']]
    assert group_anagrams([]) == []

if __name__ == "__main__":
    test_group_anagrams()