class StringHashing:
    """
    Polynomial Rolling Hash for string matching and comparison
    Supports multiple hash functions for collision resistance
    """
    
    def __init__(self, s, bases=None, mods=None):
        """
        Initialize string hashing
        
        Args:
            s: input string
            bases: list of base values for hashing (default: [31, 37])
            mods: list of modulo values (default: [10^9+7, 10^9+9])
        """
        self.s = s
        self.n = len(s)
        
        if bases is None:
            self.bases = [31, 37]
        else:
            self.bases = bases
            
        if mods is None:
            self.mods = [1000000007, 1000000009]
        else:
            self.mods = mods
        
        self.num_hashes = len(self.bases)
        
        # Precompute powers and inverse powers
        self.powers = []
        self.inv_powers = []
        self.prefix_hash = []
        
        for i in range(self.num_hashes):
            base = self.bases[i]
            mod = self.mods[i]
            
            # Compute powers
            powers = [1] * (self.n + 1)
            for j in range(1, self.n + 1):
                powers[j] = (powers[j - 1] * base) % mod
            self.powers.append(powers)
            
            # Compute inverse powers
            inv_powers = [1] * (self.n + 1)
            inv_powers[self.n] = self.mod_inverse(powers[self.n], mod)
            for j in range(self.n - 1, -1, -1):
                inv_powers[j] = (inv_powers[j + 1] * base) % mod
            self.inv_powers.append(inv_powers)
            
            # Compute prefix hashes
            prefix = [0] * self.n
            for j in range(self.n):
                char_val = ord(s[j]) - ord('a') + 1  # 1-indexed character values
                prefix[j] = (char_val * powers[j]) % mod
                if j > 0:
                    prefix[j] = (prefix[j] + prefix[j - 1]) % mod
            self.prefix_hash.append(prefix)
    
    def mod_inverse(self, a, mod):
        """Compute modular inverse using Fermat's little theorem"""
        return pow(a, mod - 2, mod)
    
    def substring_hash(self, l, r):
        """
        Get hash of substring s[l:r+1] (inclusive)
        
        Args:
            l: left index (0-indexed)
            r: right index (0-indexed, inclusive)
            
        Returns:
            list of hash values for each hash function
        """
        if l > r or l < 0 or r >= self.n:
            return [0] * self.num_hashes
        
        hashes = []
        for i in range(self.num_hashes):
            mod = self.mods[i]
            
            # Get prefix hash
            val1 = self.prefix_hash[i][r]
            val2 = self.prefix_hash[i][l - 1] if l > 0 else 0
            
            # Normalize to remove left shift
            hash_val = ((val1 - val2) % mod * self.inv_powers[i][l]) % mod
            hashes.append(hash_val)
        
        return hashes
    
    def compare_substrings(self, l1, r1, l2, r2):
        """
        Compare two substrings by hash
        
        Returns:
            True if substrings are equal (by hash), False otherwise
        """
        hash1 = self.substring_hash(l1, r1)
        hash2 = self.substring_hash(l2, r2)
        return hash1 == hash2
    
    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of pattern in the string
        
        Args:
            pattern: pattern string to search for
            
        Returns:
            list of starting indices where pattern occurs
        """
        if len(pattern) > self.n:
            return []
        
        pattern_hasher = StringHashing(pattern, self.bases, self.mods)
        pattern_hash = pattern_hasher.substring_hash(0, len(pattern) - 1)
        
        occurrences = []
        pattern_len = len(pattern)
        
        for i in range(self.n - pattern_len + 1):
            substring_hash = self.substring_hash(i, i + pattern_len - 1)
            if substring_hash == pattern_hash:
                occurrences.append(i)
        
        return occurrences
    
    def longest_common_prefix(self, i, j):
        """
        Find length of longest common prefix starting at positions i and j
        
        Args:
            i, j: starting positions
            
        Returns:
            length of longest common prefix
        """
        if i >= self.n or j >= self.n:
            return 0
        
        left, right = 0, min(self.n - i, self.n - j)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.compare_substrings(i, i + mid - 1, j, j + mid - 1):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result


class DoubleStringHashing:
    """
    String hashing with two hash functions for better collision resistance
    """
    
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.hasher = StringHashing(s, [31, 37], [1000000007, 1000000009])
    
    def get_hash(self, l, r):
        """Get hash tuple for substring"""
        hashes = self.hasher.substring_hash(l, r)
        return tuple(hashes)
    
    def are_equal(self, l1, r1, l2, r2):
        """Check if two substrings are equal"""
        return self.get_hash(l1, r1) == self.get_hash(l2, r2)


def rabin_karp(text, pattern):
    """
    Rabin-Karp algorithm for pattern matching
    
    Args:
        text: text string
        pattern: pattern to search for
        
    Returns:
        list of starting indices where pattern occurs
    """
    if len(pattern) > len(text):
        return []
    
    base = 31
    mod = 1000000007
    
    # Compute hash of pattern
    pattern_hash = 0
    for i, char in enumerate(pattern):
        pattern_hash = (pattern_hash + (ord(char) - ord('a') + 1) * pow(base, i, mod)) % mod
    
    # Compute hash of first window
    window_hash = 0
    for i in range(len(pattern)):
        window_hash = (window_hash + (ord(text[i]) - ord('a') + 1) * pow(base, i, mod)) % mod
    
    occurrences = []
    if window_hash == pattern_hash:
        occurrences.append(0)
    
    # Rolling hash
    highest_power = pow(base, len(pattern) - 1, mod)
    
    for i in range(len(pattern), len(text)):
        # Remove leftmost character
        window_hash = (window_hash - (ord(text[i - len(pattern)]) - ord('a') + 1)) % mod
        window_hash = (window_hash * pow(base, mod - 2, mod)) % mod  # Divide by base
        
        # Add rightmost character
        window_hash = (window_hash + (ord(text[i]) - ord('a') + 1) * highest_power) % mod
        
        if window_hash == pattern_hash:
            occurrences.append(i - len(pattern) + 1)
    
    return occurrences


def z_algorithm_with_hashing(s):
    """
    Use string hashing to implement Z-algorithm functionality
    Find all positions where prefixes match
    """
    n = len(s)
    hasher = StringHashing(s)
    z = [0] * n
    z[0] = n
    
    for i in range(1, n):
        # Binary search for longest prefix match
        left, right = 0, n - i
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if hasher.compare_substrings(0, mid - 1, i, i + mid - 1):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        z[i] = result
    
    return z


# Applications and utilities

def find_all_palindromic_substrings_hash(s):
    """
    Find all palindromic substrings using hash comparison
    """
    n = len(s)
    forward_hasher = StringHashing(s)
    reverse_hasher = StringHashing(s[::-1])
    
    palindromes = []
    
    for center in range(n):
        # Odd length palindromes
        left, right = 0, min(center, n - 1 - center)
        max_radius = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Check if s[center-mid:center+mid+1] is palindrome
            if (center - mid >= 0 and center + mid < n and
                forward_hasher.compare_substrings(center - mid, center + mid, 
                                                n - 1 - (center + mid), n - 1 - (center - mid))):
                max_radius = mid
                left = mid + 1
            else:
                right = mid - 1
        
        for r in range(max_radius + 1):
            palindromes.append((center - r, center + r))
    
    for center in range(n - 1):
        # Even length palindromes
        left, right = 0, min(center + 1, n - 1 - center - 1)
        max_radius = -1
        
        while left <= right:
            mid = (left + right) // 2
            # Check if s[center-mid:center+mid+2] is palindrome
            if (center - mid >= 0 and center + mid + 1 < n and
                forward_hasher.compare_substrings(center - mid, center + mid + 1,
                                                n - 1 - (center + mid + 1), n - 1 - (center - mid))):
                max_radius = mid
                left = mid + 1
            else:
                right = mid - 1
        
        for r in range(max_radius + 1):
            palindromes.append((center - r, center + r + 1))
    
    return palindromes


def longest_common_substring_hash(s1, s2):
    """
    Find longest common substring using binary search + hashing
    """
    hasher1 = StringHashing(s1)
    hasher2 = StringHashing(s2)
    
    def has_common_substring(length):
        """Check if there's a common substring of given length"""
        hashes1 = set()
        for i in range(len(s1) - length + 1):
            hash_val = tuple(hasher1.substring_hash(i, i + length - 1))
            hashes1.add(hash_val)
        
        for i in range(len(s2) - length + 1):
            hash_val = tuple(hasher2.substring_hash(i, i + length - 1))
            if hash_val in hashes1:
                return True
        return False
    
    left, right = 0, min(len(s1), len(s2))
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if has_common_substring(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Test functions
def test_string_hashing():
    """Test string hashing functionality"""
    print("Testing String Hashing:")
    
    s = "abcabcabc"
    hasher = StringHashing(s)
    
    print(f"String: {s}")
    
    # Test substring hashing
    print("Substring hashes:")
    for i in range(len(s)):
        for j in range(i, len(s)):
            hash_val = hasher.substring_hash(i, j)
            print(f"  s[{i}:{j+1}] = '{s[i:j+1]}' -> {hash_val}")
    
    # Test substring comparison
    print("\nSubstring comparisons:")
    print(f"s[0:3] == s[3:6]: {hasher.compare_substrings(0, 2, 3, 5)}")
    print(f"s[0:3] == s[6:9]: {hasher.compare_substrings(0, 2, 6, 8)}")
    print(f"s[0:2] == s[3:5]: {hasher.compare_substrings(0, 1, 3, 4)}")
    
    # Test pattern finding
    pattern = "abc"
    occurrences = hasher.find_all_occurrences(pattern)
    print(f"\nOccurrences of '{pattern}': {occurrences}")


def test_rabin_karp():
    """Test Rabin-Karp algorithm"""
    print("\nTesting Rabin-Karp:")
    
    text = "aabaacaadaabaaba"
    pattern = "aaba"
    
    occurrences = rabin_karp(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Occurrences: {occurrences}")


if __name__ == "__main__":
    test_string_hashing()
    test_rabin_karp()
