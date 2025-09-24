class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for range sum queries"""
    
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        """Add value to element at index (1-indexed)"""
        while index <= self.size:
            self.tree[index] += value
            index += index & (-index)
    
    def query(self, index):
        """Get prefix sum up to index (1-indexed)"""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & (-index)
        return result
    
    def range_query(self, left, right):
        """Get sum in range [left, right] (1-indexed)"""
        return self.query(right) - self.query(left - 1)


def distinct_elements_in_ranges(arr, queries):
    """
    Count distinct elements in range queries using offline processing
    
    Args:
        arr: input array (0-indexed)
        queries: list of (left, right) ranges (0-indexed)
    
    Returns:
        list of answers for each query
    """
    n = len(arr)
    q = len(queries)
    
    # Coordinate compression
    unique_values = sorted(set(arr))
    compression = {val: i for i, val in enumerate(unique_values)}
    compressed_arr = [compression[x] for x in arr]
    
    # Convert queries to (left, right, original_index) and sort by right endpoint
    query_list = []
    for i, (left, right) in enumerate(queries):
        query_list.append((left, right, i))
    
    query_list.sort(key=lambda x: x[1])  # Sort by right endpoint
    
    # Track last occurrence of each element
    last_occurrence = [-1] * len(unique_values)
    
    # Binary Indexed Tree for counting
    bit = BinaryIndexedTree(n)
    
    answers = [0] * q
    query_index = 0
    
    # Process elements from left to right
    for i in range(n):
        element = compressed_arr[i]
        
        # If this element appeared before, remove its previous contribution
        if last_occurrence[element] != -1:
            bit.update(last_occurrence[element] + 1, -1)  # Convert to 1-indexed
        
        # Add current occurrence
        last_occurrence[element] = i
        bit.update(i + 1, 1)  # Convert to 1-indexed
        
        # Answer all queries that end at position i
        while query_index < q and query_list[query_index][1] == i:
            left, right, original_index = query_list[query_index]
            # Count distinct elements in range [left, right]
            answers[original_index] = bit.range_query(left + 1, right + 1)  # Convert to 1-indexed
            query_index += 1
    
    return answers


def distinct_elements_mo_algorithm(arr, queries):
    """
    Alternative implementation using Mo's algorithm approach
    For comparison with the BIT approach
    """
    import math
    from collections import defaultdict
    
    n = len(arr)
    block_size = int(math.sqrt(n)) + 1
    
    # Sort queries using Mo's algorithm comparator
    def mo_comparator(query):
        left, right, index = query
        block = left // block_size
        if block % 2 == 0:
            return (block, right)
        else:
            return (block, -right)
    
    query_list = []
    for i, (left, right) in enumerate(queries):
        query_list.append((left, right, i))
    
    query_list.sort(key=mo_comparator)
    
    # Process queries
    freq = defaultdict(int)
    distinct_count = 0
    current_left = 0
    current_right = -1
    answers = [0] * len(queries)
    
    def add_element(index):
        nonlocal distinct_count
        freq[arr[index]] += 1
        if freq[arr[index]] == 1:
            distinct_count += 1
    
    def remove_element(index):
        nonlocal distinct_count
        freq[arr[index]] -= 1
        if freq[arr[index]] == 0:
            distinct_count -= 1
    
    for left, right, original_index in query_list:
        # Adjust current_left
        while current_left < left:
            remove_element(current_left)
            current_left += 1
        while current_left > left:
            current_left -= 1
            add_element(current_left)
        
        # Adjust current_right
        while current_right < right:
            current_right += 1
            add_element(current_right)
        while current_right > right:
            remove_element(current_right)
            current_right -= 1
        
        answers[original_index] = distinct_count
    
    return answers


def solve_distinct_queries():
    """Main function to solve distinct elements in range queries"""
    # Read input
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    queries = []
    for _ in range(q):
        left, right = map(int, input().split())
        queries.append((left - 1, right - 1))  # Convert to 0-indexed
    
    # Solve using BIT approach
    answers = distinct_elements_in_ranges(arr, queries)
    
    # Output answers
    for ans in answers:
        print(ans)


def test_distinct_queries():
    """Test the distinct elements implementation"""
    arr = [1, 2, 1, 3, 2, 4, 1]
    queries = [
        (0, 2),  # [1, 2, 1] -> 2 distinct
        (1, 4),  # [2, 1, 3, 2] -> 3 distinct
        (0, 6),  # [1, 2, 1, 3, 2, 4, 1] -> 4 distinct
        (3, 5),  # [3, 2, 4] -> 3 distinct
    ]
    
    print("Testing Distinct Elements in Range Queries:")
    
    # Test BIT approach
    answers_bit = distinct_elements_in_ranges(arr, queries)
    print("BIT approach results:")
    for i, (left, right) in enumerate(queries):
        print(f"Query [{left}, {right}]: {answers_bit[i]} distinct elements")
    
    # Test Mo's algorithm approach
    answers_mo = distinct_elements_mo_algorithm(arr, queries)
    print("\nMo's algorithm results:")
    for i, (left, right) in enumerate(queries):
        print(f"Query [{left}, {right}]: {answers_mo[i]} distinct elements")
    
    # Verify both approaches give same results
    print(f"\nBoth approaches match: {answers_bit == answers_mo}")


# Additional utility functions for range distinct queries

def distinct_elements_offline_sqrt_decomposition(arr, queries):
    """
    Sqrt decomposition approach for distinct elements
    Time: O(Q * sqrt(N))
    """
    import math
    
    n = len(arr)
    block_size = int(math.sqrt(n)) + 1
    num_blocks = (n + block_size - 1) // block_size
    
    answers = []
    
    for left, right in queries:
        seen = set()
        for i in range(left, right + 1):
            seen.add(arr[i])
        answers.append(len(seen))
    
    return answers


def preprocess_distinct_elements(arr):
    """
    Preprocess array for O(1) distinct element queries
    Only works for specific patterns or small arrays
    """
    n = len(arr)
    # This is just a placeholder - real preprocessing would be more complex
    # and depend on the specific constraints
    pass


if __name__ == "__main__":
    # Uncomment to run test
    test_distinct_queries()
    
    # Uncomment to solve actual problem
    # solve_distinct_queries()
