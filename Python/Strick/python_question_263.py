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
    Groups anagrams together from a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is a list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If the key exists, append the string to the corresponding list
        else:
            anagram_groups[sorted_s] = [s]  # If the key doesn't exist, create a new list with the string

    return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list

# Test cases
def test_solution():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tea', 'eat', 'ate'], ['tan', 'nat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['ate', 'tea', 'eat'], ['tan', 'nat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['tea', 'eat', 'ate']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['ate', 'tea', 'eat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['tea', 'eat', 'ate']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['ate', 'tea', 'eat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] or \
           group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['ate', 'tea', 'eat'], ['bat']]

    assert group_anagrams([""]) == [[""]]

    assert group_anagrams(["a"]) == [["a"]]

    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]

    assert group_anagrams(["aaaaaaaaaaaaaaaaaaaaaaaaaaaaab","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]) == [['aaaaaaaaaaaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']]

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()