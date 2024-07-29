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
            anagram_groups[sorted_s].append(s)  # Add the string to the existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group with the string

    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists

# Test cases
def test_group_anagrams():
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["listen", "silent", "enlist"], [["listen", "silent", "enlist"]]),
        (["dog", "god", "cat", "tac"], [["dog", "god"], ["cat", "tac"]]),
        ([], []),
        (["abc", "bca", "cba", "xyz", "zyx"], [["abc", "bca", "cba"], ["xyz", "zyx"]])
    ]

    for input_list, expected_output in test_cases:
        actual_output = group_anagrams(input_list)

        # Sort each sublist within the output to ensure consistent comparison
        for sublist in actual_output:
            sublist.sort()
        for sublist in expected_output:
            sublist.sort()
        actual_output.sort()
        expected_output.sort()

        assert actual_output == expected_output, f"Input: {input_list}, Expected: {expected_output}, Actual: {actual_output}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()