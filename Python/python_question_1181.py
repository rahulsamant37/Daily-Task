# Python Question: Word Break with Word Frequency
'''
Given a string `s` and a dictionary of words `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.  Each word in the dictionary can be used multiple times.

Additionally, each word in `wordDict` has a corresponding frequency. You are given a dictionary `wordFrequencies` where keys are words and values are their frequencies.

The segmentation is valid if the frequency of each word used in the segmentation does not exceed its corresponding frequency in `wordFrequencies`.

Input:
s = "leetcode"
wordDict = ["leet", "code"]
wordFrequencies = {"leet": 1, "code": 1}

Output:
True

Input:
s = "leetcode"
wordDict = ["leet", "code"]
wordFrequencies = {"leet": 1, "code": 0}

Output:
False

Input:
s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
wordFrequencies = {"aaaa": 1, "aaa": 1}

Output:
True

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
wordFrequencies = {"cats": 1, "dog": 1, "sand": 1, "and": 1, "cat": 1}
Output:
False
'''

# Solution
def solution():
    def wordBreak(s, wordDict, wordFrequencies):
        """
        Determines if a string can be segmented into words from a dictionary,
        respecting word frequencies.

        Args:
            s: The input string.
            wordDict: A list of words that can be used.
            wordFrequencies: A dictionary of word frequencies.

        Returns:
            True if the string can be segmented, False otherwise.
        """

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always valid

        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word:
                    # Check if the substring matches the word
                    if dp[i - len(word)]:
                        # If the substring before the word is also valid
                        # Create a temporary frequency counter
                        temp_frequencies = wordFrequencies.copy()
                        
                        # Simulate using the word and check frequency
                        valid_freq = True
                        freq_count = {}
                        
                        def count_words(string, word_list):
                            counts = {}
                            for w in word_list:
                                count = 0
                                index = 0
                                while index < len(string):
                                    index = string.find(w, index)
                                    if index == -1:
                                        break
                                    count += 1
                                    index += len(w)
                                counts[w] = count
                            return counts
                        
                        
                        # Extract the segmented string up to index i and count frequencies
                        segmented_string = s[:i]
                        words_used = []
                        
                        def backtrack(index, current_words):
                            nonlocal valid_freq
                            if index == 0:
                                return True
                            
                            for word in wordDict:
                                if index >= len(word) and s[index - len(word):index] == word:
                                    if backtrack(index - len(word), current_words + [word]):
                                        return True
                            return False

                        backtrack(i, [])
                            
                        words_used = []
                        def find_words(index):
                            if index == 0:
                                return []

                            for word in wordDict:
                                if index >= len(word) and s[index - len(word):index] == word and dp[index - len(word)]:
                                    return find_words(index - len(word)) + [word]
                            return None
                        
                        words_used = find_words(i)
                        
                        if words_used is None:
                            continue
                            
                        counts = {}
                        for word in wordDict:
                            counts[word] = words_used.count(word)
                        
                        for word, count in counts.items():
                            if word in temp_frequencies and count > temp_frequencies[word]:
                                valid_freq = False
                                break
                        
                        if valid_freq:
                            dp[i] = True
                            break
        return dp[n]
    
    return wordBreak
    

# Test cases
def test_solution():
    word_break = solution()
    
    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    wordFrequencies1 = {"leet": 1, "code": 1}
    assert word_break(s1, wordDict1, wordFrequencies1) == True

    # Test case 2
    s2 = "leetcode"
    wordDict2 = ["leet", "code"]
    wordFrequencies2 = {"leet": 1, "code": 0}
    assert word_break(s2, wordDict2, wordFrequencies2) == False

    # Test case 3
    s3 = "aaaaaaa"
    wordDict3 = ["aaaa", "aaa"]
    wordFrequencies3 = {"aaaa": 1, "aaa": 1}
    assert word_break(s3, wordDict3, wordFrequencies3) == True
    
    # Test case 4
    s4 = "catsandog"
    wordDict4 = ["cats", "dog", "sand", "and", "cat"]
    wordFrequencies4 = {"cats": 1, "dog": 1, "sand": 1, "and": 1, "cat": 1}
    assert word_break(s4, wordDict4, wordFrequencies4) == False

    # Test case 5
    s5 = "applepenapple"
    wordDict5 = ["apple", "pen"]
    wordFrequencies5 = {"apple": 2, "pen": 1}
    assert word_break(s5, wordDict5, wordFrequencies5) == True

    # Test case 6
    s6 = "applepenapple"
    wordDict6 = ["apple", "pen"]
    wordFrequencies6 = {"apple": 1, "pen": 1}
    assert word_break(s6, wordDict6, wordFrequencies6) == False

    # Test case 7
    s7 = "cars"
    wordDict7 = ["car","ca","rs"]
    wordFrequencies7 = {"car":1, "ca":1, "rs":1}
    assert word_break(s7, wordDict7, wordFrequencies7) == True

    # Test case 8
    s8 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict8 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    wordFrequencies8 = {"a": 100, "aa": 100, "aaa": 100, "aaaa": 100, "aaaaa": 100, "aaaaaa": 100, "aaaaaaa": 100, "aaaaaaaa": 100, "aaaaaaaaa": 100, "aaaaaaaaaa": 100}
    assert word_break(s8, wordDict8, wordFrequencies8) == False

    # Test case 9
    s9 = "aabbcc"
    wordDict9 = ["aa", "bb", "cc"]
    wordFrequencies9 = {"aa": 1, "bb": 1, "cc": 1}
    assert word_break(s9, wordDict9, wordFrequencies9) == True

    # Test case 10: empty string
    s10 = ""
    wordDict10 = ["a"]
    wordFrequencies10 = {"a": 1}
    assert word_break(s10, wordDict10, wordFrequencies10) == True

    # Test case 11
    s11 = "abab"
    wordDict11 = ["ab", "ba"]
    wordFrequencies11 = {"ab": 1, "ba": 1}
    assert word_break(s11, wordDict11, wordFrequencies11) == False

    print("All test cases passed!")
    

if __name__ == "__main__":
    test_solution()