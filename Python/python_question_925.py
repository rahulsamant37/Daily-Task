# Python Question: Implement a LRU Cache
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

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
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs for O(1) access
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Adds a node to the head of the list."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Removes a node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Moves a node to the head of the list."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Removes and returns the last node from the list."""
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key: int) -> int:
        """
        Gets the value of the key if the key exists in the cache, otherwise return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)  # Move the accessed node to the head
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Sets or inserts the value if the key is not already present.
        When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value  # Update the value
            self._move_to_head(node) # Move the updated node to the head
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node(node)  # Add the new node to the head

            if len(self.cache) > self.capacity:
                # Evict the least recently used node (tail)
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]

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