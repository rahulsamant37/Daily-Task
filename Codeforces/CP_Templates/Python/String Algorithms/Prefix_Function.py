def compute_prefix_function(pattern):
    """
    Compute the prefix function (failure function) for KMP algorithm
    
    Args:
        pattern: input string pattern
        
    Returns:
        prefix function array where pi[i] is the length of the longest 
        proper prefix of pattern[0:i+1] which is also a suffix
    """
    n = len(pattern)
    pi = [0] * n
    
    for i in range(1, n):
        j = pi[i - 1]
        
        # While there's a mismatch, fallback using the prefix function
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        # If characters match, increment the length
        if pattern[i] == pattern[j]:
            j += 1
        
        pi[i] = j
    
    return pi


def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt string matching algorithm
    Time complexity: O(n + m) where n = len(text), m = len(pattern)
    
    Args:
        text: text string to search in
        pattern: pattern string to search for
        
    Returns:
        list of starting indices where pattern occurs in text
    """
    if not pattern or not text:
        return []
    
    pi = compute_prefix_function(pattern)
    matches = []
    
    j = 0  # Index for pattern
    for i in range(len(text)):  # Index for text
        # While there's a mismatch, use the prefix function to skip
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            j += 1
        
        # If we've matched the entire pattern
        if j == len(pattern):
            matches.append(i - len(pattern) + 1)
            j = pi[j - 1]  # Continue searching for overlapping matches
    
    return matches


def kmp_search_first_occurrence(text, pattern):
    """
    Find only the first occurrence of pattern in text
    
    Returns:
        index of first occurrence, or -1 if not found
    """
    if not pattern or not text:
        return -1
    
    pi = compute_prefix_function(pattern)
    
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == len(pattern):
            return i - len(pattern) + 1
    
    return -1


def count_occurrences(text, pattern):
    """
    Count total number of (possibly overlapping) occurrences
    
    Returns:
        number of occurrences
    """
    return len(kmp_search(text, pattern))


def find_all_periods(s):
    """
    Find all periods of a string using prefix function
    A period p means s[i] = s[i+p] for all valid i
    
    Returns:
        list of all periods
    """
    n = len(s)
    pi = compute_prefix_function(s)
    
    periods = []
    
    # The length of the shortest period is n - pi[n-1]
    k = n - pi[n - 1]
    
    # All periods are of the form n - pi[i-1] where pi[i-1] divides n
    current = n
    while current > 0:
        period_length = current - pi[current - 1]
        if current % period_length == 0:
            periods.append(period_length)
        current = pi[current - 1]
    
    periods.reverse()
    return periods


def is_periodic(s):
    """
    Check if string has a period (is a repetition of some substring)
    
    Returns:
        (is_periodic, period_length)
    """
    n = len(s)
    pi = compute_prefix_function(s)
    
    period_length = n - pi[n - 1]
    is_periodic = (n % period_length == 0) and (period_length < n)
    
    return is_periodic, period_length if is_periodic else n


def compute_z_function(s):
    """
    Compute Z-function using prefix function approach
    Z[i] = length of longest substring starting from s[i] which is also prefix of s
    
    Returns:
        Z-array
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    
    # Use prefix function on s + '#' + s to compute Z-values
    for i in range(1, n):
        # Create string s[i:] + '#' + s and compute prefix function
        temp = s[i:] + '#' + s
        pi = compute_prefix_function(temp)
        z[i] = pi[-1]
    
    return z


def find_border_lengths(s):
    """
    Find all border lengths (lengths of strings that are both prefix and suffix)
    
    Returns:
        list of border lengths in decreasing order
    """
    pi = compute_prefix_function(s)
    borders = []
    
    current = pi[-1]
    while current > 0:
        borders.append(current)
        current = pi[current - 1]
    
    return borders


def string_matching_with_wildcards(text, pattern, wildcard='?'):
    """
    String matching where pattern can contain wildcards
    Wildcard matches any single character
    
    Returns:
        list of starting indices where pattern matches
    """
    matches = []
    
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if pattern[j] != wildcard and pattern[j] != text[i + j]:
                match = False
                break
        if match:
            matches.append(i)
    
    return matches


def multiple_pattern_search(text, patterns):
    """
    Search for multiple patterns simultaneously
    
    Args:
        text: text to search in
        patterns: list of patterns to search for
        
    Returns:
        dictionary mapping pattern to list of occurrence indices
    """
    results = {}
    
    for pattern in patterns:
        results[pattern] = kmp_search(text, pattern)
    
    return results


def longest_prefix_suffix_overlap(s1, s2):
    """
    Find the longest prefix of s1 that is also a suffix of s2
    
    Returns:
        length of longest overlap
    """
    # Create combined string s2 + '#' + s1 and find prefix function
    combined = s2 + '#' + s1
    pi = compute_prefix_function(combined)
    
    # The answer is the prefix function value at the end
    return pi[-1]


def can_be_concatenated(s, parts):
    """
    Check if string s can be formed by concatenating strings from parts list
    
    Returns:
        True if possible, False otherwise
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for part in parts:
            if i >= len(part) and dp[i - len(part)]:
                # Check if s[i-len(part):i] matches part using KMP
                if s[i - len(part):i] == part:
                    dp[i] = True
                    break
    
    return dp[n]


# Applications and utility functions

def find_all_rotations_positions(s, rotation):
    """
    Find all positions where rotation of s appears in s+s
    
    Returns:
        list of rotation positions
    """
    doubled = s + s
    matches = kmp_search(doubled, rotation)
    
    # Filter out matches that go beyond the original string length
    valid_matches = [pos for pos in matches if pos < len(s)]
    return valid_matches


def minimum_string_rotation(s):
    """
    Find the lexicographically smallest rotation of string s
    
    Returns:
        (minimum_rotation, starting_position)
    """
    n = len(s)
    doubled = s + s
    
    min_rotation = s
    min_pos = 0
    
    for i in range(n):
        rotation = doubled[i:i + n]
        if rotation < min_rotation:
            min_rotation = rotation
            min_pos = i
    
    return min_rotation, min_pos


# Test functions
def test_prefix_function():
    """Test prefix function computation"""
    print("Testing Prefix Function:")
    
    test_strings = [
        "abcabcab",
        "aabaaba", 
        "abab",
        "aaaaaa",
        "abcdef"
    ]
    
    for s in test_strings:
        pi = compute_prefix_function(s)
        print(f"String: '{s}'")
        print(f"Prefix function: {pi}")
        print()


def test_kmp_search():
    """Test KMP string matching"""
    print("Testing KMP Search:")
    
    text = "ababcababa"
    patterns = ["ab", "aba", "cab", "xyz"]
    
    print(f"Text: '{text}'")
    
    for pattern in patterns:
        matches = kmp_search(text, pattern)
        count = len(matches)
        print(f"Pattern '{pattern}': {matches} (count: {count})")


def test_string_periods():
    """Test string periodicity"""
    print("\nTesting String Periods:")
    
    test_strings = ["abcabcabc", "aabaaba", "abababab", "abcdef"]
    
    for s in test_strings:
        is_per, period = is_periodic(s)
        periods = find_all_periods(s)
        print(f"String: '{s}'")
        print(f"Is periodic: {is_per}, period length: {period}")
        print(f"All periods: {periods}")
        print()


if __name__ == "__main__":
    test_prefix_function()
    test_kmp_search()
    test_string_periods()
