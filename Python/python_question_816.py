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
    Groups a list of strings into sublists where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is a list of anagrams
    
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to use as a key. Anagrams will have the same sorted string.
        
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # If the sorted string is already a key, append the current string to its list.
        else:
            anagram_groups[sorted_s] = [s]  # If the sorted string is not a key, create a new list with the current string.
    
    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists.

# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or group_anagrams(["ate", "eat", "tea"], ['nat', 'tan'], ['bat'])
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'abc', 'cba'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'abc', 'bca'], ['xyz', 'zyx']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['bca', 'abc', 'cba'], ['zyx', 'xyz']] or group_anagrams(["abc", "bca", "cba", "xyz", "zyx"]) == [['cba', 'abc', 'bca'], ['zyx', 'xyz']]
    assert group_anagrams(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()