class SegmentTree:
    """
    Segment Tree with Point Updates and Range Queries
    Supports multiple operations with just a change in the Node and Update classes
    """
    
    def __init__(self, arr):
        self.arr = arr[:]
        self.n = len(arr)
        self.s = 1
        while self.s < 2 * self.n:
            self.s <<= 1
        self.tree = [Node() for _ in range(self.s)]
        self.build(0, self.n - 1, 1)
    
    def build(self, start, end, index):
        """Build the segment tree"""
        if start == end:
            self.tree[index] = Node(self.arr[start])
            return
        
        mid = (start + end) // 2
        self.build(start, mid, 2 * index)
        self.build(mid + 1, end, 2 * index + 1)
        self.tree[index].merge(self.tree[2 * index], self.tree[2 * index + 1])
    
    def update(self, start, end, index, query_index, update_obj):
        """Point update in the segment tree"""
        if start == end:
            update_obj.apply(self.tree[index])
            return
        
        mid = (start + end) // 2
        if mid >= query_index:
            self.update(start, mid, 2 * index, query_index, update_obj)
        else:
            self.update(mid + 1, end, 2 * index + 1, query_index, update_obj)
        
        self.tree[index].merge(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, start, end, index, left, right):
        """Range query in the segment tree"""
        if start > right or end < left:
            return Node()
        
        if start >= left and end <= right:
            return self.tree[index]
        
        mid = (start + end) // 2
        l = self.query(start, mid, 2 * index, left, right)
        r = self.query(mid + 1, end, 2 * index + 1, left, right)
        
        ans = Node()
        ans.merge(l, r)
        return ans
    
    def make_update(self, index, val):
        """Make a point update at given index"""
        update_obj = Update(val)
        self.update(0, self.n - 1, 1, index, update_obj)
    
    def make_query(self, left, right):
        """Make a range query from left to right (inclusive)"""
        return self.query(0, self.n - 1, 1, left, right)


class Node:
    """Node structure for segment tree operations"""
    
    def __init__(self, val=0):
        self.val = val  # Initialize with identity element or given value
    
    def merge(self, left, right):
        """Merge two child nodes - modify this based on the operation needed"""
        self.val = left.val ^ right.val  # XOR operation - change as needed


class Update:
    """Update structure for point updates"""
    
    def __init__(self, val):
        self.val = val
    
    def apply(self, node):
        """Apply update to the given node"""
        node.val = self.val


# Example usage for different operations:

class SumNode:
    """Node for sum queries"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        self.val = left.val + right.val


class MinNode:
    """Node for minimum queries"""
    def __init__(self, val=float('inf')):
        self.val = val
    
    def merge(self, left, right):
        self.val = min(left.val, right.val)


class MaxNode:
    """Node for maximum queries"""
    def __init__(self, val=float('-inf')):
        self.val = val
    
    def merge(self, left, right):
        self.val = max(left.val, right.val)


class XorNode:
    """Node for XOR queries"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        self.val = left.val ^ right.val


# Template for different segment tree types
class SegmentTreeTemplate:
    """Template class - inherit and override Node and Update as needed"""
    
    @staticmethod
    def create_sum_tree(arr):
        """Create a segment tree for sum queries"""
        # Replace Node and Update with SumNode and appropriate update
        pass
    
    @staticmethod
    def create_min_tree(arr):
        """Create a segment tree for minimum queries"""
        # Replace Node and Update with MinNode and appropriate update
        pass


# Test the segment tree
def test_segment_tree():
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    
    # Test range query
    result = st.make_query(1, 3)
    print(f"XOR of elements from index 1 to 3: {result.val}")
    
    # Test point update
    st.make_update(2, 10)
    result = st.make_query(1, 3)
    print(f"XOR after updating index 2 to 10: {result.val}")


if __name__ == "__main__":
    test_segment_tree()
