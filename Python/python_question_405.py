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
        A list of lists, where each sublist contains anagrams.
    """

    # Create a dictionary to store anagrams. The key will be the sorted string (canonical form),
    # and the value will be a list of strings that are anagrams of that key.
    anagram_groups = {}

    # Iterate through each string in the input list.
    for s in strs:
        # Sort the string to create its canonical form.  Anagrams will have the same sorted string.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the current string to the list of anagrams for that key.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new entry in the dictionary with the sorted string as the key and a list containing the current string as the value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    # Test case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]
    actual1 = group_anagrams(strs1)
    # Compare lengths first, then sort each sublist for reliable comparison
    assert len(actual1) == len(expected1)
    actual1_sorted = [sorted(group) for group in actual1]
    expected1_sorted = [sorted(group) for group in expected1]
    assert sorted(actual1_sorted) == sorted(expected1_sorted), f"Test Case 1 Failed: Expected {expected1}, got {actual1}"

    # Test case 2
    strs2 = [""]
    expected2 = [[""]]
    actual2 = group_anagrams(strs2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"

    # Test case 3
    strs3 = ["a"]
    expected3 = [["a"]]
    actual3 = group_anagrams(strs3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"

    # Test case 4
    strs4 = ["listen", "silent", "enlist", "tinsel"]
    expected4 = [["listen", "silent", "enlist"], ["tinsel"]]
    actual4 = group_anagrams(strs4)

    assert len(actual4) == len(expected4)
    actual4_sorted = [sorted(group) for group in actual4]
    expected4_sorted = [sorted(group) for group in expected4]
    assert sorted(actual4_sorted) == sorted(expected4_sorted), f"Test Case 4 Failed: Expected {expected4}, got {actual4}"


    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()