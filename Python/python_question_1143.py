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
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node(0, 0) # Dummy head node
        self.tail = Node(0, 0) # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If key exists in cache
        if key in self.cache:
            node = self.cache[key]
            # Move the node to the head (most recently used)
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # If key exists, update the value and move to head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # If cache is full, remove the least recently used node (tail.prev)
            if len(self.cache) == self.capacity:
                node_to_remove = self.tail.prev
                self._remove(node_to_remove)
                del self.cache[node_to_remove.key]

            # Create a new node and add it to the head
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node

    def _remove(self, node: Node) -> None:
        # Remove the node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        # Add the node to the head of the doubly linked list
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

    cache2 = LRUCache(1)
    cache2.put(2, 1)
    assert cache2.get(2) == 1
    cache2.put(3, 2)
    assert cache2.get(2) == -1
    assert cache2.get(3) == 2

    cache3 = LRUCache(3)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.put(3, 3)
    cache3.put(4, 4)
    assert cache3.get(4) == 4
    assert cache3.get(3) == 3
    assert cache3.get(2) == 2
    assert cache3.get(1) == -1
    cache3.put(5, 5)
    assert cache3.get(1) == -1
    assert cache3.get(2) == 2
    assert cache3.get(3) == 3
    assert cache3.get(4) == -1
    assert cache3.get(5) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()