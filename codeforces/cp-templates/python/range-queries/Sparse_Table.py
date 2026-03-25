import math

class SparseTable:
    """
    Sparse Table for range queries
    O(1) for idempotent operations, O(logN) for general operations
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.a = arr[:]
        self.max_log = int(math.log2(self.n)) + 1
        
        # Precompute log values
        self.log_values = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_values[i] = self.log_values[i // 2] + 1
        
        # Initialize table
        self.table = [[Node() for _ in range(self.max_log)] for _ in range(self.n)]
        self.build()
    
    def build(self):
        """Build the sparse table"""
        # Fill for length 1
        for i in range(self.n):
            self.table[i][0] = Node(self.a[i])
        
        # Fill for lengths 2, 4, 8, ...
        for j in range(1, self.max_log):
            i = 0
            while i + (1 << j) <= self.n:
                self.table[i][j] = Node()
                self.table[i][j].merge(
                    self.table[i][j - 1],
                    self.table[i + (1 << (j - 1))][j - 1]
                )
                i += 1
    
    def query_normal(self, left, right):
        """General query for any operation (O(logN))"""
        ans = Node()
        length = right - left + 1
        
        for j in range(self.log_values[length], -1, -1):
            if (1 << j) <= length:
                temp = Node()
                temp.merge(ans, self.table[left][j])
                ans = temp
                left += (1 << j)
                length -= (1 << j)
        
        return ans
    
    def query_idempotent(self, left, right):
        """Idempotent query (O(1)) - for operations like min, max, gcd"""
        j = self.log_values[right - left + 1]
        ans = Node()
        ans.merge(self.table[left][j], self.table[right - (1 << j) + 1][j])
        return ans


class Node:
    """Node structure for sparse table operations"""
    
    def __init__(self, val=0):
        self.val = val  # Identity element or given value
    
    def merge(self, left, right):
        """Merge two nodes - modify this based on the operation needed"""
        self.val = left.val ^ right.val  # XOR operation - change as needed


# Example implementations for different operations:

class MinNode:
    """Node for minimum queries (idempotent)"""
    def __init__(self, val=float('inf')):
        self.val = val
    
    def merge(self, left, right):
        self.val = min(left.val, right.val)


class MaxNode:
    """Node for maximum queries (idempotent)"""
    def __init__(self, val=float('-inf')):
        self.val = val
    
    def merge(self, left, right):
        self.val = max(left.val, right.val)


class GcdNode:
    """Node for GCD queries (idempotent)"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        import math
        self.val = math.gcd(left.val, right.val)


class SumNode:
    """Node for sum queries (not idempotent)"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        self.val = left.val + right.val


class XorNode:
    """Node for XOR queries (not idempotent)"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        self.val = left.val ^ right.val


# Specialized sparse table classes
class MinSparseTable(SparseTable):
    """Sparse Table for range minimum queries"""
    def __init__(self, arr):
        super().__init__(arr)
        # Override the table initialization
        self.table = [[MinNode() for _ in range(self.max_log)] for _ in range(self.n)]
        self.build_min()
    
    def build_min(self):
        """Build with MinNode"""
        for i in range(self.n):
            self.table[i][0] = MinNode(self.a[i])
        
        for j in range(1, self.max_log):
            i = 0
            while i + (1 << j) <= self.n:
                self.table[i][j] = MinNode()
                self.table[i][j].merge(
                    self.table[i][j - 1],
                    self.table[i + (1 << (j - 1))][j - 1]
                )
                i += 1
    
    def query_min(self, left, right):
        """O(1) minimum query"""
        j = self.log_values[right - left + 1]
        ans = MinNode()
        ans.merge(self.table[left][j], self.table[right - (1 << j) + 1][j])
        return ans.val


class MaxSparseTable(SparseTable):
    """Sparse Table for range maximum queries"""
    def __init__(self, arr):
        super().__init__(arr)
        self.table = [[MaxNode() for _ in range(self.max_log)] for _ in range(self.n)]
        self.build_max()
    
    def build_max(self):
        """Build with MaxNode"""
        for i in range(self.n):
            self.table[i][0] = MaxNode(self.a[i])
        
        for j in range(1, self.max_log):
            i = 0
            while i + (1 << j) <= self.n:
                self.table[i][j] = MaxNode()
                self.table[i][j].merge(
                    self.table[i][j - 1],
                    self.table[i + (1 << (j - 1))][j - 1]
                )
                i += 1
    
    def query_max(self, left, right):
        """O(1) maximum query"""
        j = self.log_values[right - left + 1]
        ans = MaxNode()
        ans.merge(self.table[left][j], self.table[right - (1 << j) + 1][j])
        return ans.val


# Test the sparse table
def test_sparse_table():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # Test generic sparse table with XOR
    st = SparseTable(arr)
    result = st.query_normal(2, 5)
    print(f"XOR of elements from index 2 to 5: {result.val}")
    
    # Test minimum sparse table
    min_st = MinSparseTable(arr)
    min_result = min_st.query_min(2, 5)
    print(f"Minimum of elements from index 2 to 5: {min_result}")
    
    # Test maximum sparse table
    max_st = MaxSparseTable(arr)
    max_result = max_st.query_max(2, 5)
    print(f"Maximum of elements from index 2 to 5: {max_result}")


if __name__ == "__main__":
    test_sparse_table()
