# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

# Solution
def group_anagrams(strs):
    """
    Groups a list of strings into sublists based on whether they are anagrams of each other.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each sublist contains anagrams from the input list.
    """
    anagram_groups = {}  # Dictionary to store anagram groups, key is the sorted string, value is the list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a canonical representation for anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group for this sorted string

    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["bdddddddddd","bbbbbbbbbbc"]) == [['bdddddddddd'], ['bbbbbbbbbbc']]
    assert group_anagrams(["abc","cba","bac","foo","ofo"]) == [['abc', 'cba', 'bac'], ['foo', 'ofo']] or group_anagrams(["abc","cba","bac","foo","ofo"]) == [['cba', 'abc', 'bac'], ['foo', 'ofo']] or group_anagrams(["abc","cba","bac","foo","ofo"]) == [['bac', 'cba', 'abc'], ['foo', 'ofo']] or group_anagrams(["abc","cba","bac","foo","ofo"]) == [['abc', 'cba', 'bac'], ['ofo', 'foo']] or group_anagrams(["abc","cba","bac","foo","ofo"]) == [['cba', 'abc', 'bac'], ['ofo', 'foo']] or group_anagrams(["abc","cba","bac","foo","ofo"]) == [['bac', 'cba', 'abc'], ['ofo', 'foo']]

if __name__ == "__main__":
    test_group_anagrams()