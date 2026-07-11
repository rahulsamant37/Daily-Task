# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
'''

# Solution
from collections import deque

def solution():
    def word_ladder(beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: A list of valid words.

        Returns:
            The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0

    return word_ladder


# Test cases
def test_solution():
    word_ladder = solution()  # Get the function from the solution

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","dot"]
    expected4 = 3
    assert word_ladder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected 3, Got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["slit","bunk","wars","ping","viva","wynn","wows","irks","ward","cops","nibs","owns","kopp","tows","zine","pans","hurl","wary","pled","stun","skeg","tatty","rota","eons","bill","wisp","kiln","eras","dopy","erai","miss","golf","woks","ying","fort","pies","mite","skit","coco","tack","gals","peas","roes","wuss","rowl","rice","tripe","lawn","chair","bags","nude","lgbt","vows","awab","prom","tides","oils","boon","cmsn","wail","moss","legs","sore","rile","wood","pond","tops","gags","ingot","peck","teds","pals","rows","beds","lime","womb","blob","view","rips","peas","rime","gees","lard","vows","auto","crew","mesh","urea","rand","snug","hips","tows","lass","iowa","surf","kits","cols","laud","shoo","pows","tops","shun","dopy","erie","gums","dewy","tows","wags","wren","rope","wolf","warp","male","play","ants","sire","tusk","boss","tags","wean","lass","rags","mina","weet","tune","gaff","cage","wisp","robe","from","jaws","wank","donk","czar","aves","rips","gasps","waif","crus","woes","ruses","pals","hays","stim","wing","nuts","wail","shun","awry","cake","sand","yams","apps","nary"," закономерности","автомат","cars","числитель","wore","exploits","избирательность","sand","зима","dopy","sams","дим","tugs","esse","wants","модель","топология","автомат","автоматизация","машина","амортизация","бабочка","гипотеза","модуль","вектор","поддержка","изложение","уравнение","система","комплекс","вероятность","актуальный","избирательность","устойчивость","адаптация","математика","компьютер","технология","разработка","управление","автоматический","анализ","эффективность","интеллект","управление","контроль","информация","моделирование","оптимизация","алгоритм","прогноз","оценка","исследование","эксперимент","программа","наука","техника","инновации","развитие","производство","качество","энергия","ресурс","безопасность","экология","экономика","политика","общество","культура","образование","медицина","право","история","философия","психология","социология","литература","искусство","музыка","театр","кино","телевидение","радио","интернет","спорт","туризм","путешествия","отдых","развлечения","хобби","коллекционирование","кулинария","сад","огород","дом","семья","дети","друзья","любовь","счастье","здоровье","красота","мода","стиль","финансы","работа","карьера","бизнес","маркетинг","реклама","продажи","услуги","клиенты","партнеры","конкуренты","рынок","торговля","транспорт","логистика","склад","производство","технология","оборудование","материалы","сырье","полуфабрикаты","готовая продукция","упаковка","маркировка","сертификация","лицензирование","стандартизация","метрология","контроль качества","управление качеством","обеспечение качества","бережливое производство","шесть сигм","реинжиниринг бизнес-процессов","управление проектами","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями","управление качеством","управление рисками","управление изменениями","управление знаниями","управление персоналом","управление финансами","управление маркетингом","управление производством","управление запасами","управление логистикой","управление поставками","управление взаимоотношениями с клиентами","управление взаимоотношениями с поставщиками","управление инновациями"]
    expected5 = 8
    assert word_ladder(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()