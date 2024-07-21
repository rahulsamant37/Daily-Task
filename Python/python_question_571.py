# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups anagrams together in a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    # Create a dictionary to store the sorted string as the key and the list of anagrams as the value.
    anagram_groups = {}

    # Iterate through the list of strings.
    for str_val in strs:
        # Sort the string to create a canonical representation of the anagram.
        sorted_str = "".join(sorted(str_val))

        # If the sorted string is already a key in the dictionary, append the current string to the list of anagrams.
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(str_val)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the current string as the value.
        else:
            anagram_groups[sorted_str] = [str_val]

    # Return the list of lists of anagrams.
    return list(anagram_groups.values())

# Test cases
def test_solution():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['oof', 'foo']]

if __name__ == "__main__":
    test_solution()