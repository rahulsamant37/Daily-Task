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
    Groups anagrams together in a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_map = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams

        if sorted_s in anagram_map:
            anagram_map[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_map[sorted_s] = [s]  # Create a new anagram group with the string

    return list(anagram_map.values())  # Return the list of anagram groups

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']]
    assert group_anagrams([]) == []
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()