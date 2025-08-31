"""
Simple Heap Implementation in Python
====================================

A heap is a binary tree where parent nodes are always smaller (min-heap) 
or larger (max-heap) than their children.

Key Properties:
- Complete binary tree (filled left to right)
- Parent at index i, children at 2*i+1 and 2*i+2
- Min-heap: parent <= children
"""

class MinHeap:
    """Simple Min-Heap implementation using a list."""
    
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        """Add a value to the heap."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
    
    def pop(self):
        """Remove and return the minimum value."""
        if not self.heap:
            return None
        
        # Move last element to root, then bubble down
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._bubble_down(0)
        
        return min_val
    
    def peek(self):
        """Return minimum value without removing it."""
        return self.heap[0] if self.heap else None
    
    def _bubble_up(self, index):
        """Move element up until heap property is satisfied."""
        if index == 0:
            return
        
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)
    
    def _bubble_down(self, index):
        """Move element down until heap property is satisfied."""
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        
        # Find smallest among parent and children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        # If parent is not smallest, swap and continue
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)
    
    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)


# Example Usage
if __name__ == "__main__":
    # Create a min-heap
    heap = MinHeap()
    
    # Add elements
    for num in [5, 2, 8, 1, 9, 3]:
        heap.push(num)
        print(f"Added {num}: {heap}")
    
    # Remove elements (will come out in sorted order)
    print("\nRemoving elements:")
    while len(heap) > 0:
        min_val = heap.pop()
        print(f"Removed {min_val}: {heap}")
    
    # Using Python's built-in heapq (alternative)
    import heapq
    
    print("\nUsing built-in heapq:")
    nums = [5, 2, 8, 1, 9, 3]
    heapq.heapify(nums)  # Convert list to heap
    print(f"Heapified: {nums}")
    
    while nums:
        print(f"Pop: {heapq.heappop(nums)}, Remaining: {nums}")