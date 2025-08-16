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
    Groups a list of strings into sublists, where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups, key is sorted string, value is list of anagrams

    for s in strs:
        # Sort the string to create a unique key for anagrams
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the original string to the list
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the original string as the value
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists
    return list(anagram_groups.values())


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [["abc", "cba", "bac"], ["foo", "oof"]]
    assert group_anagrams([]) == []
    print("All test cases passed!")


if __name__ == "__main__":
    test_group_anagrams()