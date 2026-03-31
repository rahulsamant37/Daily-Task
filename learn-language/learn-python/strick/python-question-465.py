# Python Question: Implement a Least Recently Used (LRU) Cache
'''
Design and implement a data structure for a Least Recently Used (LRU) cache.

Implement the LRUCache class:

*   `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
*   `int get(int key)` Return the value of the key if the key exists in the cache, otherwise return -1.
*   `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions `get` and `put` must both run in O(1) average time complexity.

Example:

Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, 2, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

# Solution
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node()  # Dummy head node
        self.tail = Node()  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        # Remove a node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        # Add a node to the beginning of the doubly linked list (after head)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # Get the value of the key if the key exists in the cache
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the node to the beginning (most recently used)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists, otherwise add the key-value pair to the cache
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

            if len(self.cache) > self.capacity:
                # Evict the least recently used key (the node before the tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]


# Test cases
def test_solution():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4

    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)
    assert lRUCache.get(2) == 1
    lRUCache.put(3, 2)
    assert lRUCache.get(2) == -1
    assert lRUCache.get(3) == 2

    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(2) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()