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
class LRUCache:

    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with the given capacity.
        Uses a dictionary to store the key-value pairs and a doubly linked list to maintain the order of usage.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = Node(0, 0)  # Dummy head node of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail node of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # Current size of the cache

    def get(self, key: int) -> int:
        """
        Gets the value of the key if the key exists in the cache, otherwise returns -1.
        If the key exists, it moves the key to the head of the doubly linked list to mark it as recently used.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)  # Remove the node from its current position
            self._add_to_head(node)  # Add the node to the head of the list
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Sets or inserts the value if the key is not already present.
        When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.
        """
        if key in self.cache:
            # If the key exists, update its value and move it to the head
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # If the key doesn't exist, create a new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1

            if self.size > self.capacity:
                # If the cache is full, remove the least recently used item (the tail)
                tail_node = self.tail.prev
                self._remove_node(tail_node)
                del self.cache[tail_node.key]
                self.size -= 1

    def _add_to_head(self, node: 'Node'):
        """
        Adds a node to the head of the doubly linked list.
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: 'Node'):
        """
        Removes a node from the doubly linked list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

class Node:
    """
    Represents a node in the doubly linked list.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

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