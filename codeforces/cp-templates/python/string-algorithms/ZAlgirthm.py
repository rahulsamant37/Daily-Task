def z_function(s):
    """
    Z-algorithm implementation
    z[i] = length of longest substring starting from s[i] which is also prefix of s
    Time complexity: O(n)
    
    Args:
        s: input string
        
    Returns:
        z array where z[i] is length of longest common prefix of s and s[i:]
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def z_algorithm_search(text, pattern):
    """
    Use Z-algorithm for pattern matching
    
    Args:
        text: text string to search in
        pattern: pattern to search for
        
    Returns:
        list of starting indices where pattern occurs
    """
    if not pattern or not text:
        return []
    
    # Create combined string: pattern + '#' + text
    combined = pattern + '#' + text
    z = z_function(combined)
    
    matches = []
    pattern_len = len(pattern)
    
    # Look for Z-values equal to pattern length
    for i in range(pattern_len + 1, len(combined)):
        if z[i] == pattern_len:
            # Found match at position i - pattern_len - 1 in original text
            matches.append(i - pattern_len - 1)
    
    return matches

def count_distinct_substrings_z(s):
    """
    Count number of distinct substrings using Z-algorithm
    
    Returns:
        number of distinct substrings
    """
    n = len(s)
    distinct_count = 0
    
    for i in range(n):
        suffix = s[i:]
        z = z_function(suffix)
        
        # For each position, count new substrings
        for j in range(len(suffix)):
            if j == 0 or z[j] < j:
                distinct_count += 1
    
    return distinct_count

def longest_common_prefix_z(s1, s2):
    """
    Find longest common prefix using Z-algorithm
    
    Returns:
        length of longest common prefix
    """
    combined = s1 + '#' + s2
    z = z_function(combined)
    
    # LCP is the maximum Z-value in the second part
    return max(z[len(s1) + 1:]) if len(z) > len(s1) + 1 else 0

def periodic_string_z(s):
    """
    Find the shortest period of string using Z-algorithm
    
    Returns:
        length of shortest period
    """
    z = z_function(s)
    n = len(s)
    
    for period in range(1, n):
        if period + z[period] == n:
            return period
    
    return n

def all_occurrences_z(text, pattern):
    """
    Find all occurrences with additional information
    
    Returns:
        list of (position, match_length) tuples
    """
    combined = pattern + '#' + text
    z = z_function(combined)
    
    results = []
    pattern_len = len(pattern)
    
    for i in range(pattern_len + 1, len(combined)):
        if z[i] > 0:
            text_pos = i - pattern_len - 1
            results.append((text_pos, z[i]))
    
    return results

def z_to_prefix_function(z):
    """
    Convert Z-array to prefix function array
    
    Returns:
        prefix function array
    """
    n = len(z)
    pi = [0] * n
    
    for i in range(1, n):
        for j in range(z[i] - 1, -1, -1):
            if pi[i + j] == 0:
                pi[i + j] = j + 1
            else:
                break
    
    return pi

def prefix_to_z_function(pi):
    """
    Convert prefix function array to Z-array
    
    Returns:
        Z-array
    """
    n = len(pi)
    z = [0] * n
    
    for i in range(1, n):
        if pi[i] > 0:
            z[i - pi[i] + 1] = pi[i]
    
    # Fill remaining values
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        # This is a simplified reconstruction
        # Full reconstruction would need the original string
    
    return z

def find_borders_z(s):
    """
    Find all border lengths using Z-algorithm
    A border is a string that is both prefix and suffix
    
    Returns:
        list of border lengths
    """
    z = z_function(s)
    n = len(s)
    borders = []
    
    for i in range(1, n):
        if i + z[i] == n:
            borders.append(z[i])
    
    borders.sort(reverse=True)
    return borders

def string_factorization_z(s):
    """
    Factorize string into Lyndon words using Z-algorithm
    
    Returns:
        list of factors
    """
    n = len(s)
    factors = []
    i = 0
    
    while i < n:
        z = z_function(s[i:])
        
        # Find the longest prefix that is also a suffix
        j = 1
        while j < len(z) and i + j < n:
            if z[j] > 0 and j + z[j] == len(z):
                break
            j += 1
        
        factors.append(s[i:i + j])
        i += j
    
    return factors

def main_lorentz_z(s):
    """
    Find main Lorentz period using Z-algorithm
    
    Returns:
        main period length
    """
    z = z_function(s)
    n = len(s)
    
    for i in range(1, n):
        if z[i] + i == n and n % i == 0:
            return i
    
    return n

# Test functions
def test_z_algorithm():
    """Test Z-algorithm implementation"""
    print("Testing Z-Algorithm:")
    
    test_strings = [
        "abacaba",
        "aabaaba", 
        "abcabcab",
        "aaaaaa"
    ]
    
    for s in test_strings:
        z = z_function(s)
        print(f"String: '{s}'")
        print(f"Z-array: {z}")
        print()

def test_pattern_matching():
    """Test pattern matching with Z-algorithm"""
    print("Testing Pattern Matching:")
    
    text = "ababcababa"
    patterns = ["ab", "aba", "cab", "xyz"]
    
    print(f"Text: '{text}'")
    
    for pattern in patterns:
        matches = z_algorithm_search(text, pattern)
        print(f"Pattern '{pattern}': {matches}")

def test_string_properties():
    """Test string property functions"""
    print("\nTesting String Properties:")
    
    # Test periodicity
    periodic_strings = ["abcabcabc", "aabaaba", "abababab"]
    
    for s in periodic_strings:
        period = periodic_string_z(s)
        borders = find_borders_z(s)
        print(f"String: '{s}'")
        print(f"Shortest period: {period}")
        print(f"Borders: {borders}")
        print()

if __name__ == "__main__":
    test_z_algorithm()
    test_pattern_matching()
    test_string_properties()
