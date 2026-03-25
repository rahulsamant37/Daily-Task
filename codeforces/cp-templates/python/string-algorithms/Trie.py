class TrieNode:
    """Node for Trie data structure"""
    
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False
        self.count = 0  # Number of words ending at this node
        self.prefix_count = 0  # Number of words passing through this node
    
    def __repr__(self):
        return f"TrieNode(children={list(self.children.keys())}, is_end={self.is_end_of_word}, count={self.count})"


class Trie:
    """
    Trie (Prefix Tree) data structure for efficient string operations
    """
    
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
    
    def insert(self, word):
        """
        Insert a word into the trie
        Time complexity: O(m) where m is length of word
        
        Args:
            word: string to insert
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        
        if not node.is_end_of_word:
            self.word_count += 1
        node.is_end_of_word = True
        node.count += 1
    
    def search(self, word):
        """
        Search for a word in the trie
        Time complexity: O(m)
        
        Args:
            word: string to search for
            
        Returns:
            True if word exists, False otherwise
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if any word in trie starts with given prefix
        Time complexity: O(m)
        
        Args:
            prefix: prefix string
            
        Returns:
            True if prefix exists, False otherwise
        """
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix):
        """
        Find the node corresponding to a prefix
        
        Returns:
            TrieNode if prefix exists, None otherwise
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def delete(self, word):
        """
        Delete a word from the trie
        Time complexity: O(m)
        
        Args:
            word: string to delete
            
        Returns:
            True if word was deleted, False if word didn't exist
        """
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.count = 0
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete_child = _delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child:
                node.children[char].prefix_count -= 1
                if node.children[char].prefix_count == 0:
                    del node.children[char]
            
            return (not node.is_end_of_word and 
                    len(node.children) == 0 and 
                    node != self.root)
        
        if self.search(word):
            _delete_helper(self.root, word, 0)
            self.word_count -= 1
            return True
        return False
    
    def get_all_words(self):
        """
        Get all words in the trie
        
        Returns:
            list of all words
        """
        result = []
        
        def dfs(node, current_word):
            if node.is_end_of_word:
                result.append(current_word)
            
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(self.root, "")
        return result
    
    def get_words_with_prefix(self, prefix):
        """
        Get all words that start with given prefix
        
        Args:
            prefix: prefix string
            
        Returns:
            list of words with the prefix
        """
        prefix_node = self._find_node(prefix)
        if prefix_node is None:
            return []
        
        result = []
        
        def dfs(node, current_word):
            if node.is_end_of_word:
                result.append(current_word)
            
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(prefix_node, prefix)
        return result
    
    def count_words_with_prefix(self, prefix):
        """
        Count number of words that start with given prefix
        
        Returns:
            number of words with the prefix
        """
        prefix_node = self._find_node(prefix)
        return prefix_node.prefix_count if prefix_node else 0
    
    def longest_common_prefix(self):
        """
        Find the longest common prefix of all words in trie
        
        Returns:
            longest common prefix string
        """
        node = self.root
        prefix = ""
        
        while (len(node.children) == 1 and 
               not node.is_end_of_word and 
               node != self.root):
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        
        return prefix
    
    def autocomplete(self, prefix, max_suggestions=10):
        """
        Get autocomplete suggestions for a prefix
        
        Args:
            prefix: prefix to complete
            max_suggestions: maximum number of suggestions
            
        Returns:
            list of suggested completions
        """
        suggestions = self.get_words_with_prefix(prefix)
        return suggestions[:max_suggestions]


class BinaryTrie:
    """
    Binary Trie for integer operations (XOR operations, etc.)
    """
    
    def __init__(self, max_bits=32):
        self.root = {}
        self.max_bits = max_bits
    
    def insert(self, num):
        """Insert a number into binary trie"""
        node = self.root
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def find_max_xor(self, num):
        """Find maximum XOR with any number in trie"""
        node = self.root
        max_xor = 0
        
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            # Try to go to opposite bit for maximum XOR
            opposite_bit = 1 - bit
            
            if opposite_bit in node:
                max_xor |= (1 << i)
                node = node[opposite_bit]
            elif bit in node:
                node = node[bit]
            else:
                break
        
        return max_xor


class SuffixTrie:
    """
    Suffix Trie for string matching and pattern searching
    """
    
    def __init__(self, text):
        self.text = text
        self.trie = Trie()
        self._build_suffix_trie()
    
    def _build_suffix_trie(self):
        """Build suffix trie from text"""
        for i in range(len(self.text)):
            suffix = self.text[i:] + f"${i}"  # Add unique terminator
            self.trie.insert(suffix)
    
    def contains_pattern(self, pattern):
        """Check if pattern exists in text"""
        return self.trie.starts_with(pattern)
    
    def find_all_occurrences(self, pattern):
        """Find all occurrences of pattern in text"""
        if not self.contains_pattern(pattern):
            return []
        
        # Find all suffixes that start with pattern
        matching_suffixes = self.trie.get_words_with_prefix(pattern)
        positions = []
        
        for suffix in matching_suffixes:
            # Extract position from terminator
            pos = int(suffix.split('$')[-1])
            positions.append(pos)
        
        return sorted(positions)


# Applications and utility functions

def find_longest_word(words):
    """Find the longest word that can be built one character at a time"""
    trie = Trie()
    
    # Insert all words
    for word in words:
        trie.insert(word)
    
    def can_build(word):
        for i in range(1, len(word)):
            if not trie.search(word[:i]):
                return False
        return True
    
    longest = ""
    for word in words:
        if can_build(word) and len(word) > len(longest):
            longest = word
    
    return longest

def word_break(s, word_dict):
    """Check if string can be segmented into dictionary words"""
    trie = Trie()
    for word in word_dict:
        trie.insert(word)
    
    def can_break(start):
        if start == len(s):
            return True
        
        node = trie.root
        for i in range(start, len(s)):
            if s[i] not in node.children:
                break
            node = node.children[s[i]]
            if node.is_end_of_word and can_break(i + 1):
                return True
        
        return False
    
    return can_break(0)

def replace_words(dictionary, sentence):
    """Replace words with their shortest root from dictionary"""
    trie = Trie()
    for root in dictionary:
        trie.insert(root)
    
    def find_root(word):
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.is_end_of_word:
                return word[:i + 1]
        return word
    
    words = sentence.split()
    return ' '.join(find_root(word) for word in words)


# Test functions
def test_trie():
    """Test basic trie operations"""
    print("Testing Trie:")
    
    trie = Trie()
    words = ["apple", "app", "apricot", "banana", "band", "bandana"]
    
    # Insert words
    for word in words:
        trie.insert(word)
    
    print(f"Inserted words: {words}")
    print(f"Total words in trie: {trie.word_count}")
    
    # Test search
    test_words = ["app", "apple", "appl", "banana", "ban"]
    for word in test_words:
        found = trie.search(word)
        print(f"Search '{word}': {found}")
    
    # Test prefix search
    prefixes = ["app", "ban", "xyz"]
    for prefix in prefixes:
        has_prefix = trie.starts_with(prefix)
        count = trie.count_words_with_prefix(prefix)
        words_with_prefix = trie.get_words_with_prefix(prefix)
        print(f"Prefix '{prefix}': exists={has_prefix}, count={count}, words={words_with_prefix}")
    
    # Test autocomplete
    suggestions = trie.autocomplete("ap", 3)
    print(f"Autocomplete 'ap': {suggestions}")

def test_binary_trie():
    """Test binary trie for XOR operations"""
    print("\nTesting Binary Trie:")
    
    btrie = BinaryTrie()
    numbers = [3, 10, 5, 25, 2]
    
    for num in numbers:
        btrie.insert(num)
    
    print(f"Numbers: {numbers}")
    
    for num in numbers:
        max_xor = btrie.find_max_xor(num)
        print(f"Max XOR with {num}: {max_xor}")

if __name__ == "__main__":
    test_trie()
    test_binary_trie()
