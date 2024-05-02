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
        A list of lists, where each inner list contains anagrams.
    """

    # Create a dictionary to store the sorted string as key and the list of anagrams as value.
    anagram_groups = {}

    # Iterate through the input list of strings.
    for s in strs:
        # Sort the string alphabetically to identify anagrams.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the original string to its value list.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as key and a list containing the original string as value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

    assert group_anagrams([""]) == [[""]]

    assert group_anagrams(["a"]) == [["a"]]

    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]

    assert group_anagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]) == [['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()