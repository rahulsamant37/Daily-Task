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
        A list of lists, where each sublist contains anagrams.
    """
    anagram_map = {}  # Dictionary to store anagrams. Key: sorted string, Value: list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_map:
            anagram_map[sorted_s].append(s)  # If the key exists, append the string to the existing list
        else:
            anagram_map[sorted_s] = [s]  # If the key doesn't exist, create a new list with the string

    return list(anagram_map.values())  # Return the values of the dictionary (which are the lists of anagrams)


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["", ""]) == [["", ""]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']]
    assert group_anagrams(["listen", "silent", "enlist", "tinsel"]) == [['listen', 'silent', 'enlist', 'tinsel']]
    print("All test cases passed!")


if __name__ == "__main__":
    test_group_anagrams()