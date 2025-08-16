# Python Question: Implement a Word Search Solver
'''
Given a 2D board of characters and a list of words, find all words from the list that can be found in the board.
A word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["oath","eat"]
'''

# Solution
def solution():
    def findWords(board, words):
        """
        Finds all words from a list of words that can be formed on a given board.

        Args:
            board: A 2D list of characters representing the board.
            words: A list of strings representing the words to search for.

        Returns:
            A list of strings representing the words found in the board.
        """

        def build_trie(words):
            """Builds a Trie data structure from a list of words."""
            trie = {}
            for word in words:
                node = trie
                for char in word:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                node['#'] = word  # Use '#' to mark the end of a word
            return trie

        def dfs(row, col, node, board, visited, result):
            """Performs Depth-First Search to find words in the board."""
            if '#' in node:
                word = node['#']
                result.add(word)
                node['#'] = None  # Avoid adding the same word multiple times

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            if (row, col) in visited:
                return
            char = board[row][col]
            if char not in node:
                return

            visited.add((row, col))
            dfs(row + 1, col, node[char], board, visited, result)  # Down
            dfs(row - 1, col, node[char], board, visited, result)  # Up
            dfs(row, col + 1, node[char], board, visited, result)  # Right
            dfs(row, col - 1, node[char], board, visited, result)  # Left
            visited.remove((row, col))  # Backtrack

        # Build the Trie from the words
        trie = build_trie(words)

        # Initialize variables
        result = set()
        rows = len(board)
        cols = len(board[0])

        # Iterate through the board and start DFS from each cell
        for row in range(rows):
            for col in range(cols):
                visited = set()
                dfs(row, col, trie, board, visited, result)

        return list(result)

    return findWords
    # Test cases
def test_solution():
    findWords = solution()
    board1 = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words1 = ["oath","pea","eat","rain"]
    assert sorted(findWords(board1, words1)) == sorted(["oath","eat"])

    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    assert findWords(board2, words2) == []

    board3 = [["a"]]
    words3 = ["a"]
    assert findWords(board3, words3) == ["a"]

    board4 = [["a","a"]]
    words4 = ["aaa"]
    assert findWords(board4, words4) == []

    board5 = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words5 = ["abcdefg","bcdea"]
    assert sorted(findWords(board5, words5)) == sorted(["abcdefg","bcdea"])
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()