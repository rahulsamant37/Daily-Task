"""
String Operations and Optimizations
===================================

Efficient string handling for competitive programming.
Avoid common string operation pitfalls.
"""

def string_concatenation_optimization():
    """
    Efficient ways to concatenate strings
    """
    
    # BAD: Repeated string concatenation (O(n²) time)
    def slow_concatenation(words):
        result = ""
        for word in words:
            result += word  # Creates new string each time
        return result
    
    # GOOD: Use join (O(n) time)
    def fast_concatenation(words):
        return "".join(words)
    
    # For building strings character by character
    def char_by_char_building(chars):
        return "".join(chars)
    
    # With separator
    def join_with_separator(words, sep=" "):
        return sep.join(words)
    
    return fast_concatenation, char_by_char_building

def string_searching_and_matching():
    """
    Efficient string searching operations
    """
    
    # Built-in string methods are optimized
    def basic_string_ops(text, pattern):
        # Check if pattern exists
        exists = pattern in text  # Fast C implementation
        
        # Find position
        pos = text.find(pattern)  # Returns -1 if not found
        
        # Count occurrences
        count = text.count(pattern)
        
        # Replace operations
        replaced = text.replace(pattern, "replacement")
        
        return exists, pos, count, replaced
    
    # For complex pattern matching, compile regex
    import re
    
    def regex_operations(text):
        # Compile regex once, use multiple times
        pattern = re.compile(r'\d+')  # Find all numbers
        
        matches = pattern.findall(text)
        positions = [(m.start(), m.end()) for m in pattern.finditer(text)]
        
        return matches, positions
    
    return basic_string_ops, regex_operations

def string_manipulation_tricks():
    """
    Useful string manipulation techniques
    """
    
    # Reverse string efficiently
    def reverse_string(s):
        return s[::-1]  # Slice notation is fast
    
    # Check palindrome
    def is_palindrome(s):
        return s == s[::-1]
    
    # Remove characters efficiently
    def remove_chars(s, chars_to_remove):
        # Using translate (very fast for character removal)
        translator = str.maketrans('', '', chars_to_remove)
        return s.translate(translator)
    
    # Alternative using join and filter
    def remove_chars_filter(s, chars_to_remove):
        return ''.join(c for c in s if c not in chars_to_remove)
    
    # Case operations
    def case_operations(s):
        return {
            'lower': s.lower(),
            'upper': s.upper(),
            'title': s.title(),
            'capitalize': s.capitalize(),
            'swapcase': s.swapcase()
        }
    
    return reverse_string, remove_chars, case_operations

def string_parsing_for_cp():
    """
    Common string parsing patterns in competitive programming
    """
    
    # Parse input efficiently
    def parse_multiple_integers(line):
        return list(map(int, line.split()))
    
    # Parse mixed input
    def parse_mixed_line(line):
        parts = line.split()
        n = int(parts[0])
        name = parts[1]
        values = list(map(int, parts[2:]))
        return n, name, values
    
    # Split on multiple delimiters
    import re
    def split_multiple_delims(text, delims):
        pattern = '[' + re.escape(''.join(delims)) + ']'
        return re.split(pattern, text)
    
    # Parse coordinate pairs
    def parse_coordinates(line):
        # Input: "1,2 3,4 5,6"
        pairs = line.split()
        coords = []
        for pair in pairs:
            x, y = map(int, pair.split(','))
            coords.append((x, y))
        return coords
    
    return parse_multiple_integers, parse_coordinates

def string_hashing_and_rolling_hash():
    """
    String hashing for fast string comparison
    """
    
    # Simple polynomial hash
    def polynomial_hash(s, base=31, mod=10**9 + 7):
        hash_value = 0
        power = 1
        for char in s:
            hash_value = (hash_value + ord(char) * power) % mod
            power = (power * base) % mod
        return hash_value
    
    # Rolling hash for substring matching
    class RollingHash:
        def __init__(self, text, base=31, mod=10**9 + 7):
            self.text = text
            self.base = base
            self.mod = mod
            self.n = len(text)
            
            # Precompute hash values and powers
            self.hash_vals = [0] * (self.n + 1)
            self.powers = [1] * (self.n + 1)
            
            for i in range(self.n):
                self.hash_vals[i + 1] = (self.hash_vals[i] * base + ord(text[i])) % mod
                self.powers[i + 1] = (self.powers[i] * base) % mod
        
        def get_hash(self, left, right):
            # Hash of substring text[left:right]
            result = (self.hash_vals[right] - self.hash_vals[left] * self.powers[right - left]) % self.mod
            return result if result >= 0 else result + self.mod
    
    return polynomial_hash, RollingHash

def string_algorithms():
    """
    Important string algorithms for CP
    """
    
    # KMP (Knuth-Morris-Pratt) pattern matching
    def kmp_search(text, pattern):
        # Build failure function
        def build_failure_function(pattern):
            m = len(pattern)
            failure = [0] * m
            j = 0
            
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = failure[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                failure[i] = j
            
            return failure
        
        n, m = len(text), len(pattern)
        if m == 0:
            return []
        
        failure = build_failure_function(pattern)
        matches = []
        j = 0
        
        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = failure[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                matches.append(i - m + 1)
                j = failure[j - 1]
        
        return matches
    
    # Longest Common Subsequence
    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    return kmp_search, lcs_length

def string_optimization_tips():
    """
    Key optimization tips for strings
    """
    tips = [
        "Use ''.join() instead of += for concatenation",
        "Use 'in' operator for substring search (fast C implementation)",
        "Prefer str.replace() over manual character replacement",
        "Use str.translate() for character removal/replacement",
        "Compile regex patterns if used multiple times",
        "Use string slicing s[::-1] for reversal",
        "Consider string hashing for fast equality checks",
        "Use list(map(int, line.split())) for parsing integers",
        "Cache string methods in loops (like append caching)",
        "Use str.strip() to remove whitespace efficiently"
    ]
    return tips

def common_string_patterns():
    """
    Common string manipulation patterns in CP
    """
    
    # Check if string is a rotation of another
    def is_rotation(s1, s2):
        return len(s1) == len(s2) and s1 in s2 + s2
    
    # Find all anagrams
    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    
    # Count character frequencies
    def char_frequency(s):
        from collections import Counter
        return Counter(s)
    
    # Generate all permutations of string
    def string_permutations(s):
        from itertools import permutations
        return [''.join(p) for p in permutations(s)]
    
    # Longest palindromic substring (naive)
    def longest_palindrome_naive(s):
        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(longest):
                    longest = substr
        return longest
    
    return is_rotation, are_anagrams, char_frequency, longest_palindrome_naive

if __name__ == "__main__":
    print("String Optimization Techniques")
    
    # Test concatenation
    words = ["hello", " ", "world", "!", " ", "python"]
    fast_concat, char_build = string_concatenation_optimization()
    result = fast_concat(words)
    print(f"Concatenated: '{result}'")
    
    # Test string operations
    basic_ops, _ = string_searching_and_matching()
    text = "The quick brown fox jumps over the lazy dog"
    pattern = "fox"
    exists, pos, count, replaced = basic_ops(text, pattern)
    print(f"Pattern '{pattern}' exists: {exists}, position: {pos}")
    
    # Test hashing
    poly_hash, RollingHash = string_hashing_and_rolling_hash()
    test_string = "hello"
    hash_val = poly_hash(test_string)
    print(f"Hash of '{test_string}': {hash_val}")
    
    # Test string patterns
    is_rot, are_anag, char_freq, _ = common_string_patterns()
    print(f"'abc' and 'bca' are anagrams: {are_anag('abc', 'bca')}")
    print(f"Character frequency of 'hello': {char_freq('hello')}")
    
    # Show optimization tips
    tips = string_optimization_tips()
    print("\nString Optimization Tips:")
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
