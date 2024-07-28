# Python Question: Implement a Least Recently Used (LRU) Cache
'''
Design and implement a data structure for a Least Recently Used (LRU) cache.
It should support the following operations:
- get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.

Implement the LRUCache class:
- LRUCache(int capacity) - Initialize the LRU cache with positive size capacity.
- int get(int key) - Return the value of the key if present, otherwise return -1.
- void put(int key, int value) - Update the value of the key if the key is present. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put operations in O(1) complexity?

Example:

LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

# Solution
class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the cache with a capacity and a doubly linked list and a hashmap.
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = Node(0, 0)  # Dummy head node of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail node of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Check if the key is present in the cache.
        if key in self.cache:
            # If present, move it to the head of the list (most recently used).
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            # If not present, return -1.
            return -1

    def put(self, key: int, value: int) -> None:
        # Check if the key is already present in the cache.
        if key in self.cache:
            # If present, update the value and move it to the head of the list.
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            # If not present, create a new node.
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

            # If the cache is full, remove the least recently used node (tail.prev).
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]  # Remove from the dictionary

    def _add(self, node: 'Node'):
        # Add a node to the head of the doubly linked list.
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: 'Node'):
        # Remove a node from the doubly linked list.
        node.prev.next = node.next
        node.next.prev = node.prev

class Node:
    # Helper class to represent a node in the doubly linked list.
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# Test cases
def test_solution():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(1)
    cache.put(2,1)
    assert cache.get(2) == 1
    cache.put(3,2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2
    print("All test cases passed")

if __name__ == "__main__":
    test_solution()