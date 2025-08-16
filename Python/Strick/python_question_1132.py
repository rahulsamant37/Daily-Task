# Python Question: Implement a LRU Cache
'''
Implement a Least Recently Used (LRU) cache.  The cache has a fixed capacity,
and when a new key is added and the cache is full, the least recently used key
is evicted.

The cache should support the following operations:

*   `get(key)`:  Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   `put(key, value)`: Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The LRU cache should be implemented using a dictionary (hash map) and a doubly linked list. The dictionary will store the key-value pairs along with pointers to the corresponding nodes in the linked list. The linked list will maintain the order of the keys based on their usage.

Example:

capacity = 2
lru = LRUCache(capacity)
lru.put(1, 1)
lru.put(2, 2)
lru.get(1)       # returns 1
lru.put(3, 3)    # evicts key 2
lru.get(2)       # returns -1 (not found)
lru.put(4, 4)    # evicts key 1
lru.get(1)       # returns -1 (not found)
lru.get(3)       # returns 3
lru.get(4)       # returns 4
'''

# Solution
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node()  # Dummy head node of the doubly linked list
        self.tail = Node()  # Dummy tail node of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node):
        """Adds a node to the head of the doubly linked list."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Gets the value of the key if it exists, otherwise returns -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the node to the head (most recently used)
            self._add_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Sets or inserts the value. Evicts the LRU item if necessary."""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                # Evict the least recently used item (tail.prev)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]  # Remove from the dictionary


# Test cases
def test_solution():
    capacity = 2
    lru = LRUCache(capacity)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    capacity = 1
    lru = LRUCache(capacity)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == -1
    assert lru.get(2) == 2

    capacity = 2
    lru = LRUCache(capacity)
    lru.put(2, 1)
    lru.put(1, 1)
    lru.put(2, 3)
    lru.put(4, 1)
    assert lru.get(1) == -1
    assert lru.get(2) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()