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
def solution(strs):
    """
    Groups anagrams together in a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """
    # Create a dictionary to store the sorted string as key and list of anagrams as value.
    anagram_groups = {}

    # Iterate through the input list of strings.
    for s in strs:
        # Sort the string to create a unique key for anagrams.
        sorted_s = "".join(sorted(s))

        # If the sorted string is already a key in the dictionary, append the current string to its value list.
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        # Otherwise, create a new key-value pair with the sorted string as key and a list containing the current string as value.
        else:
            anagram_groups[sorted_s] = [s]

    # Return the values of the dictionary as a list of lists.
    return list(anagram_groups.values())

# Test cases
def test_solution():
    assert solution(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['tan', 'nat'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['tea', 'eat', 'ate'], ['nat', 'tan'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'tea', 'eat'], ['nat', 'tan'], ['bat']]
    assert solution([""]) == [[""]]
    assert solution(["a"]) == [["a"]]
    assert solution(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']] or solution(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['foo', 'oof']] or solution(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['foo', 'oof']] or solution(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['oof', 'foo']] or solution(["abc", "cba", "bac", "foo", "oof"]) == [['cba', 'abc', 'bac'], ['oof', 'foo']] or solution(["abc", "cba", "bac", "foo", "oof"]) == [['bac', 'cba', 'abc'], ['oof', 'foo']]
    assert solution(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']] or solution(["listen", "silent", "enlist"]) == [['silent', 'listen', 'enlist']] or solution(["listen", "silent", "enlist"]) == [['enlist', 'silent', 'listen']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()