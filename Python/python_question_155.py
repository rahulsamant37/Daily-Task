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
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups. Key: sorted string, Value: list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key for anagram grouping.

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If the sorted string is already a key, add the string to the existing group.
        else:
            anagram_groups[sorted_s] = [s]  # If the sorted string is not a key, create a new group with the string.

    return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list.

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["a", ""]) == [['a'], ['']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']]
    assert group_anagrams(["abc", "bca", "cab", "def", "fed"]) == [['abc', 'bca', 'cab'], ['def', 'fed']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()