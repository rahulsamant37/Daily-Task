# Python Question: Implement a LRU Cache
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item *before* inserting a new item.

The cache is initialized with a *positive* capacity.

Follow up:
Could you do both operations in *O(1)* time complexity?

Example:

LRUCache cache = new LRUCache(2); // capacity 2

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
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: Node
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If the key is in the cache
        if key in self.cache:
            # Move the node to the head of the linked list (most recently used)
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        # If the key is not in the cache
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache
        if key in self.cache:
            # Update the value of the node
            node = self.cache[key]
            node.val = value
            # Move the node to the head of the linked list
            self._remove(node)
            self._add(node)
        # If the key is not in the cache
        else:
            # Create a new node
            node = Node(key, value)
            # Add the node to the cache
            self.cache[key] = node
            # Add the node to the head of the linked list
            self._add(node)
            # If the cache is full
            if len(self.cache) > self.capacity:
                # Remove the least recently used node (tail)
                tail = self.tail.prev
                self._remove(tail)
                del self.cache[tail.key]

    def _add(self, node):
        # Add the node to the head of the linked list
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        # Remove the node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev

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
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(3, 2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()