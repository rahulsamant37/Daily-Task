class LazySegmentTree:
    """
    Lazy Segment Tree with Range Updates and Range Queries
    Supports efficient range updates using lazy propagation
    """
    
    def __init__(self, arr):
        self.arr = arr[:]
        self.n = len(arr)
        self.s = 1
        while self.s < 2 * self.n:
            self.s <<= 1
        
        self.tree = [Node() for _ in range(self.s)]
        self.lazy = [False] * self.s
        self.updates = [Update() for _ in range(self.s)]
        
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
    
    def pushdown(self, index, start, end):
        """Push lazy updates down to children"""
        if self.lazy[index]:
            mid = (start + end) // 2
            self.apply(2 * index, start, mid, self.updates[index])
            self.apply(2 * index + 1, mid + 1, end, self.updates[index])
            self.updates[index] = Update()
            self.lazy[index] = False
    
    def apply(self, index, start, end, update_obj):
        """Apply update to a node"""
        if start != end:
            self.lazy[index] = True
            self.updates[index].combine(update_obj, start, end)
        update_obj.apply(self.tree[index], start, end)
    
    def update(self, start, end, index, left, right, update_obj):
        """Range update in the segment tree"""
        if start > right or end < left:
            return
        
        if start >= left and end <= right:
            self.apply(index, start, end, update_obj)
            return
        
        self.pushdown(index, start, end)
        mid = (start + end) // 2
        self.update(start, mid, 2 * index, left, right, update_obj)
        self.update(mid + 1, end, 2 * index + 1, left, right, update_obj)
        self.tree[index].merge(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, start, end, index, left, right):
        """Range query in the segment tree"""
        if start > right or end < left:
            return Node()
        
        if start >= left and end <= right:
            self.pushdown(index, start, end)
            return self.tree[index]
        
        self.pushdown(index, start, end)
        mid = (start + end) // 2
        l = self.query(start, mid, 2 * index, left, right)
        r = self.query(mid + 1, end, 2 * index + 1, left, right)
        
        ans = Node()
        ans.merge(l, r)
        return ans
    
    def make_update(self, left, right, val):
        """Make a range update from left to right (inclusive)"""
        update_obj = Update(val)
        self.update(0, self.n - 1, 1, left, right, update_obj)
    
    def make_query(self, left, right):
        """Make a range query from left to right (inclusive)"""
        return self.query(0, self.n - 1, 1, left, right)


class Node:
    """Node structure for lazy segment tree operations"""
    
    def __init__(self, val=0):
        self.val = val  # Initialize with identity element or given value
    
    def merge(self, left, right):
        """Merge two child nodes - modify this based on the operation needed"""
        self.val = left.val + right.val  # Sum operation - change as needed


class Update:
    """Update structure for range updates"""
    
    def __init__(self, val=0):
        self.val = val  # Identity update value
    
    def apply(self, node, start, end):
        """Apply update to the given node"""
        node.val = self.val * (end - start + 1)  # Range assignment - change as needed
    
    def combine(self, new_update, start, end):
        """Combine with another update"""
        self.val = new_update.val  # Override with new update - change as needed


# Example implementations for different operations:

class SumNode:
    """Node for sum queries with lazy updates"""
    def __init__(self, val=0):
        self.val = val
    
    def merge(self, left, right):
        self.val = left.val + right.val


class AddUpdate:
    """Update for range addition"""
    def __init__(self, val=0):
        self.val = val
    
    def apply(self, node, start, end):
        node.val += self.val * (end - start + 1)
    
    def combine(self, new_update, start, end):
        self.val += new_update.val


class SetUpdate:
    """Update for range assignment"""
    def __init__(self, val=0):
        self.val = val
    
    def apply(self, node, start, end):
        node.val = self.val * (end - start + 1)
    
    def combine(self, new_update, start, end):
        self.val = new_update.val


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


# Test the lazy segment tree
def test_lazy_segment_tree():
    arr = [1, 2, 3, 4, 5]
    lst = LazySegmentTree(arr)
    
    # Test range query
    result = lst.make_query(0, 4)
    print(f"Sum of all elements: {result.val}")
    
    # Test range update
    lst.make_update(1, 3, 10)  # Set elements at indices 1,2,3 to 10
    result = lst.make_query(0, 4)
    print(f"Sum after range update: {result.val}")
    
    # Test partial range query
    result = lst.make_query(1, 3)
    print(f"Sum of updated range: {result.val}")


if __name__ == "__main__":
    test_lazy_segment_tree()
