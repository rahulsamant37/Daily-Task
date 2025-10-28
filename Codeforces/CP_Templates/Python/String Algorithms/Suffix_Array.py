"""
Suffix Array Implementation
===========================

A suffix array is a sorted array of all suffixes of a string.
It's used for efficient string operations like pattern matching, 
longest common prefix, and many other string problems.

Time Complexity: O(n log n)
Space Complexity: O(n)

Author: Converted from C++ implementation
"""

def counting_sort(p, c, n):
    """
    Counting sort based on character classes
    
    Args:
        p: permutation array (suffix array)
        c: character classes
        n: length of string
    
    Returns:
        Sorted permutation array
    """
    cnt = [0] * n
    for x in c:
        cnt[x] += 1
    
    p_new = [0] * n
    pos = [0] * n
    pos[0] = 0
    for i in range(1, n):
        pos[i] = pos[i - 1] + cnt[i - 1]
    
    for x in p:
        i = c[x]
        p_new[pos[i]] = x
        pos[i] += 1
    
    return p_new

def build_suffix_array(s):
    """
    Build suffix array for string s
    
    Args:
        s: input string
    
    Returns:
        suffix array as list of integers
    """
    s += '$'  # Add sentinel character
    n = len(s)
    p = [0] * n  # suffix array
    c = [0] * n  # character classes
    
    # Initialize for single characters
    a = [(s[i], i) for i in range(n)]
    a.sort()
    
    for i in range(n):
        p[i] = a[i][1]
    
    c[p[0]] = 0
    for i in range(1, n):
        if a[i][0] == a[i - 1][0]:
            c[p[i]] = c[p[i - 1]]
        else:
            c[p[i]] = c[p[i - 1]] + 1
    
    k = 0
    while (1 << k) < n:
        # Shift positions by 2^k
        for i in range(n):
            p[i] = (p[i] - (1 << k) + n) % n
        
        # Sort using counting sort
        p = counting_sort(p, c, n)
        
        # Update character classes
        c_new = [0] * n
        c_new[p[0]] = 0
        
        for i in range(1, n):
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n])
            now = (c[p[i]], c[(p[i] + (1 << k)) % n])
            
            if now == prev:
                c_new[p[i]] = c_new[p[i - 1]]
            else:
                c_new[p[i]] = c_new[p[i - 1]] + 1
        
        k += 1
        c = c_new
    
    return p

def build_lcp_array(s, sa):
    """
    Build LCP (Longest Common Prefix) array using Kasai's algorithm
    
    Args:
        s: original string
        sa: suffix array
    
    Returns:
        LCP array
    """
    n = len(s)
    rank = [0] * n
    
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = [0] * (n - 1)
    h = 0
    
    for i in range(n):
        if rank[i] == n - 1:
            h = 0
            continue
        
        j = sa[rank[i] + 1]
        
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        
        lcp[rank[i]] = h
        
        if h > 0:
            h -= 1
    
    return lcp

def pattern_search(pattern, text):
    """
    Search for pattern in text using suffix array
    
    Args:
        pattern: pattern to search
        text: text to search in
    
    Returns:
        list of starting positions where pattern occurs
    """
    sa = build_suffix_array(text)
    n = len(text)
    m = len(pattern)
    
    # Binary search for leftmost occurrence
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        suffix = text[sa[mid]:sa[mid] + m] if sa[mid] + m <= n else text[sa[mid]:]
        if suffix < pattern:
            left = mid + 1
        else:
            right = mid
    
    start = left
    
    # Binary search for rightmost occurrence
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        suffix = text[sa[mid]:sa[mid] + m] if sa[mid] + m <= n else text[sa[mid]:]
        if suffix <= pattern:
            left = mid + 1
        else:
            right = mid
    
    end = left
    
    # Extract all occurrences
    occurrences = []
    for i in range(start, end):
        if sa[i] + m <= n and text[sa[i]:sa[i] + m] == pattern:
            occurrences.append(sa[i])
    
    return sorted(occurrences)

def longest_repeated_substring(s):
    """
    Find the longest repeated substring using suffix array
    
    Args:
        s: input string
    
    Returns:
        tuple (length, substring)
    """
    if not s:
        return 0, ""
    
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s + '$', sa)
    
    max_length = 0
    best_pos = 0
    
    for i in range(len(lcp)):
        if lcp[i] > max_length:
            max_length = lcp[i]
            best_pos = sa[i]
    
    return max_length, s[best_pos:best_pos + max_length]

def count_distinct_substrings(s):
    """
    Count number of distinct substrings using suffix array
    
    Args:
        s: input string
    
    Returns:
        number of distinct substrings
    """
    n = len(s)
    if n == 0:
        return 0
    
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s + '$', sa)
    
    # Total substrings = n*(n+1)/2
    # Subtract repeated substrings
    total = n * (n + 1) // 2
    repeated = sum(lcp)
    
    return total - repeated

def test_suffix_array():
    """Test suffix array implementation"""
    print("Testing Suffix Array Implementation")
    print("=" * 40)
    
    # Test 1: Basic suffix array
    s = "banana"
    sa = build_suffix_array(s)
    print(f"String: {s}")
    print(f"Suffix Array: {sa}")
    
    # Print all suffixes in order
    print("Suffixes in sorted order:")
    for i, pos in enumerate(sa):
        if pos < len(s):
            print(f"{i}: {s[pos:]}")
    
    print()
    
    # Test 2: LCP array
    lcp = build_lcp_array(s + '$', sa)
    print(f"LCP Array: {lcp}")
    print()
    
    # Test 3: Pattern searching
    pattern = "ana"
    occurrences = pattern_search(pattern, s)
    print(f"Pattern '{pattern}' found at positions: {occurrences}")
    print()
    
    # Test 4: Longest repeated substring
    length, substring = longest_repeated_substring(s)
    print(f"Longest repeated substring: '{substring}' (length: {length})")
    print()
    
    # Test 5: Count distinct substrings
    count = count_distinct_substrings(s)
    print(f"Number of distinct substrings: {count}")
    print()
    
    # Test 6: Another example
    s2 = "abcab"
    sa2 = build_suffix_array(s2)
    print(f"String: {s2}")
    print(f"Suffix Array: {sa2}")
    
    # Test pattern search in s2
    pattern2 = "ab"
    occurrences2 = pattern_search(pattern2, s2)
    print(f"Pattern '{pattern2}' found at positions: {occurrences2}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_suffix_array()
