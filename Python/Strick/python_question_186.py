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
        A list of lists of strings, where each sublist contains strings that are anagrams of each other.
    """

    # Create a dictionary to store anagrams.
    # The key will be the sorted string (representing the anagram group),
    # and the value will be a list of strings that belong to that group.
    anagram_groups = {}

    # Iterate through the input list of strings.
    for s in strs:
        # Sort the characters in the string to create a unique key for each anagram group.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary,
        # it means we have found another anagram.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key
        # and a list containing the current string as the value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    """
    Tests the group_anagrams function with several test cases.
    """

    # Test case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
    result1 = group_anagrams(strs1)
    # Convert lists to sets of tuples for comparison, as order doesn't matter
    result1_sets = [set(x) for x in result1]
    expected1_sets = [set(x) for x in expected1]
    assert set(tuple(sorted(s)) for s in result1_sets) == set(tuple(sorted(s)) for s in expected1_sets), f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test case 2
    strs2 = [""]
    expected2 = [[""]]
    result2 = group_anagrams(strs2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test case 3
    strs3 = ["a"]
    expected3 = [["a"]]
    result3 = group_anagrams(strs3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    # Test case 4
    strs4 = ["listen", "silent", "enlist", "tinsel"]
    expected4 = [["listen", "silent", "enlist", "tinsel"]]
    result4 = group_anagrams(strs4)
    result4_sets = [set(x) for x in result4]
    expected4_sets = [set(x) for x in expected4]
    assert set(tuple(sorted(s)) for s in result4_sets) == set(tuple(sorted(s)) for s in expected4_sets), f"Test Case 4 Failed: Expected {expected4}, got {result4}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()