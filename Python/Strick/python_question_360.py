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
    Groups a list of strings into lists of anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagram groups, keyed by sorted string.

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key.

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add to existing anagram group.
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group.

    return list(anagram_groups.values())  # Return the values (lists of anagrams).


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [['']]
    assert group_anagrams(["a"]) == [['a']]
    assert group_anagrams(["a", ""]) == [['a'], ['']]
    assert group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']]
    print("All test cases passed")

if __name__ == "__main__":
    test_group_anagrams()