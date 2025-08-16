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
    Groups a list of strings into sublists of anagrams.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}  # Dictionary to store anagrams, key is the sorted string, value is a list of anagrams
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the corresponding anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group if the sorted string is not in the dictionary

    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists

# Test cases
def test_group_anagrams():
    """
    Tests the group_anagrams function with several test cases.
    """
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["listen", "silent", "enlist", "tinsel"], [["listen", "silent", "enlist", "tinsel"]]),
        (["abc", "cab", "xyz", "zyx", "bac"], [["abc", "cab", "bac"], ["xyz", "zyx"]]),
        (["dog","god","cat"], [["dog","god"],["cat"]]),
        (["", ""], [["", ""]])
    ]

    for input_strs, expected_output in test_cases:
        actual_output = group_anagrams(input_strs)
        # Sort the inner lists to make comparison order-insensitive
        for i in range(len(actual_output)):
            actual_output[i].sort()
        for i in range(len(expected_output)):
            expected_output[i].sort()

        # Sort the output lists to make comparison order-insensitive
        actual_output.sort()
        expected_output.sort()

        assert actual_output == expected_output, f"Input: {input_strs}, Expected: {expected_output}, Actual: {actual_output}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()