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
    anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams
    
    for s in strs:
        sorted_s = "".join(sorted(s))  # Sort the string to create a unique key for anagrams
        
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)  # Add the string to the corresponding anagram group
        else:
            anagram_groups[sorted_s] = [s]  # Create a new anagram group if it doesn't exist
            
    return list(anagram_groups.values())  # Return the values of the dictionary as a list of lists

# Test cases
def test_solution():
    assert solution(["eat","tea","tan","ate","nat","bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] or solution(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['bat'], ['nat', 'tan'], ['eat', 'tea', 'ate']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['eat', 'tea', 'ate'], ['bat']] or solution(["eat","tea","tan","ate","nat","bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']]
    assert solution([""]) == [[""]]
    assert solution(["a"]) == [["a"]]
    assert solution(["abc","bca","cab","xyz","zyx"]) == [['abc', 'bca', 'cab'], ['xyz', 'zyx']] or solution(["abc","bca","cab","xyz","zyx"]) == [['bca', 'cab', 'abc'], ['xyz', 'zyx']] or solution(["abc","bca","cab","xyz","zyx"]) == [['cab', 'abc', 'bca'], ['xyz', 'zyx']] or solution(["abc","bca","cab","xyz","zyx"]) == [['xyz', 'zyx'], ['abc', 'bca', 'cab']] or solution(["abc","bca","cab","xyz","zyx"]) == [['xyz', 'zyx'], ['bca', 'cab', 'abc']] or solution(["abc","bca","cab","xyz","zyx"]) == [['xyz', 'zyx'], ['cab', 'abc', 'bca']]
    assert solution(["dog","god","cat"]) == [['dog', 'god'], ['cat']] or solution(["dog","god","cat"]) == [['god', 'dog'], ['cat']] or solution(["dog","god","cat"]) == [['cat'], ['dog', 'god']] or solution(["dog","god","cat"]) == [['cat'], ['god', 'dog']]

if __name__ == "__main__":
    test_solution()