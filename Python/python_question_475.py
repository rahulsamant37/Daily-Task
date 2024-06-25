# Python Question: Implement a Least Recently Used (LRU) Cache
'''
Design and implement a data structure for a Least Recently Used (LRU) cache. It should support the following operations:

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

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
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If the key exists in the cache
        if key in self.cache:
            node = self.cache[key]
            # Move the node to the head (most recently used)
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        # If the key already exists, update its value and move it to the head
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            # If the cache is full, remove the least recently used node (tail.prev)
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]  # Remove from cache as well

            # Create a new node and add it to the head
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node  # Add to the cache

    def _remove(self, node: Node):
        # Helper function to remove a node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        # Helper function to add a node to the head of the doubly linked list
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


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