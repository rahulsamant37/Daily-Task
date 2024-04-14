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
    Groups a list of strings into sublists, where each sublist contains anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists of strings, where each sublist contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is a list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the corresponding anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group if the key doesn't exist
    return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list

# Test cases
def test_group_anagrams():
    """
    Tests the group_anagrams function with several test cases.
    """
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["listen", "silent", "enlist", "tinsel"], [["listen", "silent", "enlist", "tinsel"]]),
        (["abc", "bac", "cab", "def"], [["abc", "bac", "cab"], ["def"]]),
        (["code", "deco"], [["code", "deco"]]),
        (["", "b"], [[""], ["b"]])
    ]

    for strs, expected in test_cases:
        result = group_anagrams(strs)
        # Sort each sublist in result and expected to ensure order doesn't matter within each group
        for sublist in result:
            sublist.sort()
        for sublist in expected:
            sublist.sort()

        # Sort the entire result and expected lists based on the first element of each sublist
        result.sort(key=lambda x: x[0] if x else "")
        expected.sort(key=lambda x: x[0] if x else "")

        assert result == expected, f"Input: {strs}, Expected: {expected}, Got: {result}"
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()