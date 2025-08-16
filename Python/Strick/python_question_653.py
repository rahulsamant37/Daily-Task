# Python Question: Group Anagrams
'''
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

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

    # Create a dictionary to store anagrams, using the sorted string as the key.
    anagram_groups = {}

    # Iterate through the input list of strings.
    for s in strs:
        # Sort the string to create a unique key for anagrams.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the original string to the corresponding list.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the original string as the value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values (lists of anagrams) from the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_solution():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) ==  [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) ==  [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

    assert group_anagrams([""]) == [[""]]

    assert group_anagrams(["a"]) == [["a"]]

    assert group_anagrams(["", ""]) == [['', '']]

    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'abc', 'cba'], ['foo', 'oof']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['oof', 'foo']] or group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'abc', 'cba'], ['oof', 'foo']]

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()