import sys
import math
from collections import defaultdict

class MoAlgorithm:
    """
    Mo's Algorithm for offline query processing
    Efficiently answers range queries by reordering them
    """
    
    def __init__(self, arr, queries):
        self.n = len(arr)
        self.arr = arr[:]
        self.queries = queries
        self.block_size = int(math.sqrt(self.n)) + 1
        
        # Coordinate compression
        self.coordinate_compression = {}
        self.compressed_arr = []
        self._compress_coordinates()
        
        # Frequency array and current answer
        self.freq = defaultdict(int)
        self.current_answer = 0
        
        # Current range
        self.current_left = 0
        self.current_right = -1
    
    def _compress_coordinates(self):
        """Compress coordinates to handle large values"""
        unique_values = sorted(set(self.arr))
        for i, val in enumerate(unique_values):
            self.coordinate_compression[val] = i + 1
        
        self.compressed_arr = [self.coordinate_compression[x] for x in self.arr]
    
    def _compare_queries(self, query):
        """Comparator function for sorting queries"""
        left, right, index = query
        block = left // self.block_size
        
        # Mo's algorithm optimization: alternate sorting direction
        if block % 2 == 0:
            return (block, right)
        else:
            return (block, -right)
    
    def _add_element(self, index):
        """Add element at index to current range"""
        val = self.compressed_arr[index]
        self.freq[val] += 1
        if self.freq[val] == 1:
            self.current_answer += 1
    
    def _remove_element(self, index):
        """Remove element at index from current range"""
        val = self.compressed_arr[index]
        self.freq[val] -= 1
        if self.freq[val] == 0:
            self.current_answer -= 1
    
    def solve(self):
        """Solve all queries using Mo's algorithm"""
        # Convert queries to (left, right, original_index) format
        query_list = []
        for i, (left, right) in enumerate(self.queries):
            query_list.append((left - 1, right - 1, i))  # Convert to 0-indexed
        
        # Sort queries according to Mo's algorithm
        query_list.sort(key=self._compare_queries)
        
        # Process queries
        answers = [0] * len(self.queries)
        
        for left, right, original_index in query_list:
            # Adjust current_left
            while self.current_left < left:
                self._remove_element(self.current_left)
                self.current_left += 1
            
            while self.current_left > left:
                self.current_left -= 1
                self._add_element(self.current_left)
            
            # Adjust current_right
            while self.current_right < right:
                self.current_right += 1
                self._add_element(self.current_right)
            
            while self.current_right > right:
                self._remove_element(self.current_right)
                self.current_right -= 1
            
            # Store answer
            answers[original_index] = self.current_answer
        
        return answers


# Example usage for different types of queries

class MoDistinctElements(MoAlgorithm):
    """Mo's Algorithm for counting distinct elements in range"""
    
    def _add_element(self, index):
        val = self.compressed_arr[index]
        self.freq[val] += 1
        if self.freq[val] == 1:
            self.current_answer += 1
    
    def _remove_element(self, index):
        val = self.compressed_arr[index]
        self.freq[val] -= 1
        if self.freq[val] == 0:
            self.current_answer -= 1


class MoSum(MoAlgorithm):
    """Mo's Algorithm for range sum queries"""
    
    def __init__(self, arr, queries):
        super().__init__(arr, queries)
        self.current_answer = 0
    
    def _add_element(self, index):
        self.current_answer += self.arr[index]
    
    def _remove_element(self, index):
        self.current_answer -= self.arr[index]


class MoXor(MoAlgorithm):
    """Mo's Algorithm for range XOR queries"""
    
    def __init__(self, arr, queries):
        super().__init__(arr, queries)
        self.current_answer = 0
    
    def _add_element(self, index):
        self.current_answer ^= self.arr[index]
    
    def _remove_element(self, index):
        self.current_answer ^= self.arr[index]


class MoSquareSum(MoAlgorithm):
    """Mo's Algorithm for sum of squares in range"""
    
    def __init__(self, arr, queries):
        super().__init__(arr, queries)
        self.current_answer = 0
    
    def _add_element(self, index):
        self.current_answer += self.arr[index] ** 2
    
    def _remove_element(self, index):
        self.current_answer -= self.arr[index] ** 2


def solve_distinct_elements():
    """Example: Count distinct elements in range queries"""
    # Input reading
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    queries = []
    for _ in range(q):
        left, right = map(int, input().split())
        queries.append((left, right))
    
    # Solve using Mo's algorithm
    mo = MoDistinctElements(arr, queries)
    answers = mo.solve()
    
    # Output answers
    for ans in answers:
        print(ans)


def test_mo_algorithm():
    """Test Mo's algorithm with sample data"""
    arr = [1, 2, 1, 3, 2, 4, 1]
    queries = [
        (1, 3),  # Elements 1,2,1 -> 2 distinct
        (2, 5),  # Elements 2,1,3,2 -> 3 distinct
        (1, 7),  # Elements 1,2,1,3,2,4,1 -> 4 distinct
        (4, 6),  # Elements 3,2,4 -> 3 distinct
    ]
    
    mo = MoDistinctElements(arr, queries)
    answers = mo.solve()
    
    print("Test Results:")
    for i, (left, right) in enumerate(queries):
        print(f"Query [{left}, {right}]: {answers[i]} distinct elements")


if __name__ == "__main__":
    # Uncomment to run test
    # test_mo_algorithm()
    
    # Uncomment to solve actual problem
    solve_distinct_elements()
