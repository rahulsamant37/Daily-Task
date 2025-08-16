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
    Groups anagrams together from a list of strings.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains anagrams.
    """

    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams

    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add to existing anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group

    return list(anagram_groups.values())  # Return the values (lists of anagrams) as a list

# Test cases
def test_solution():
    assert solution(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['tan', 'nat'], ['eat', 'tea', 'ate']]
    assert solution([""]) == [[""]]
    assert solution(["a"]) == [["a"]]
    assert solution(["abc", "bca", "cba", "xyz", "zyx"]) == [['abc', 'bca', 'cba'], ['xyz', 'zyx']] or solution(["abc", "bca", "cba", "xyz", "zyx"]) == [['xyz', 'zyx'], ['abc', 'bca', 'cba']]
    assert solution(["listen", "silent", "enlist"]) == [['listen', 'silent', 'enlist']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()