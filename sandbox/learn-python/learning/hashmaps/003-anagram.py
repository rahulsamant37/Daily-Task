def group_anagrams(words):
    anagrams = {}

    for eachWord in words:
        sorted_word = "".join(sorted(eachWord))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(eachWord)
        else:
            anagrams[sorted_word] = [eachWord]
    return list(anagrams.values())



words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))
