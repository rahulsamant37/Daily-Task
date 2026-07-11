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
        A list of lists, where each sublist contains anagrams of each other.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is the list of anagrams
    for str_val in strs:
        sorted_str = "".join(sorted(str_val))  # Sort the string to create a unique key for anagrams
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(str_val)  # If the sorted string already exists, add the current string to the list
        else:
            anagram_groups[sorted_str] = [str_val]  # If the sorted string doesn't exist, create a new list with the current string
    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']]
    assert group_anagrams([]) == []
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()