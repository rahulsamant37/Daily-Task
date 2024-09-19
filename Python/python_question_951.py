# Python Question: Group Anagrams
'''
Given a list of strings, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

# Solution
def solution():
    def group_anagrams(strs):
        """
        Groups anagrams together in a list of strings.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains anagrams.
        """
        anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams
        for s in strs:
            sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s].append(s)  # Add the string to the corresponding anagram group
            else:
                anagram_groups[sorted_s] = [s]  # Create a new anagram group for the sorted string

        return list(anagram_groups.values())  # Return the list of anagram groups

    return group_anagrams
    # Test cases
def test_solution():
    def group_anagrams(strs):
        """
        Groups anagrams together in a list of strings.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains anagrams.
        """
        anagram_groups = {}  # Dictionary to store anagrams, key is sorted string, value is list of anagrams
        for s in strs:
            sorted_s = "".join(sorted(s))  # Sort the string to identify anagrams
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s].append(s)  # Add the string to the corresponding anagram group
            else:
                anagram_groups[sorted_s] = [s]  # Create a new anagram group for the sorted string

        return list(anagram_groups.values())  # Return the list of anagram groups

    assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert group_anagrams([""]) == [['']]
    assert group_anagrams(["a"]) == [['a']]
    assert group_anagrams(["abc", "cba", "bac", "foo", "oof"]) == [['abc', 'cba', 'bac'], ['foo', 'oof']]
    assert group_anagrams(["listen", "silent", "enlist", "hello", "world"]) == [['listen', 'silent', 'enlist'], ['hello'], ['world']]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()