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
    Groups a list of strings into sublists, where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams

        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the existing group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new group for this anagram

    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists


# Test cases
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or \
           group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'eat', 'tea'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tea', 'ate', 'eat'], ['tan', 'nat'], ['bat']] or \
           group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']]  # Order doesn't matter

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert group_anagrams(["", ""]) == [["", ""]]
    assert group_anagrams(["a", ""]) == [["a"], [""]]
    assert group_anagrams(["listen", "silent"]) == [["listen", "silent"]] or group_anagrams(["listen", "silent"]) == [['silent', 'listen']]
    assert group_anagrams(["listen", "silent", "hello"]) == [["listen", "silent"], ['hello']] or group_anagrams(["listen", "silent", "hello"]) == [['silent', 'listen'], ['hello']] or group_anagrams(["listen", "silent", "hello"]) == [['hello'], ["listen", "silent"]] or group_anagrams(["listen", "silent", "hello"]) == [['hello'], ['silent', 'listen']]
    print("All test cases passed!")


if __name__ == "__main__":
    test_group_anagrams()