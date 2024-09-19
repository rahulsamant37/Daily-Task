# Python Question: Implement a LRU Cache
'''
Design and implement a data structure for a Least Recently Used (LRU) cache. It should support the following operations:

1. get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
2. put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

capacity = 2

put(1, 1)
put(2, 2)
get(1)       // returns 1
put(3, 3)    // evicts key 2
get(2)       // returns -1 (not found)
put(4, 4)    // evicts key 1
get(1)       // returns -1 (not found)
get(3)       // returns 3
get(4)       // returns 4
'''

# Solution
class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the capacity of the cache
        self.capacity = capacity
        # Use a dictionary to store the key-value pairs
        self.cache = {}
        # Use a doubly linked list to track the order of usage
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If the key is not in the cache, return -1
        if key not in self.cache:
            return -1

        # If the key is in the cache, move it to the head of the linked list
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache, update its value and move it to the head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # If the cache is full, remove the least recently used item (tail.prev)
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]

            # Add the new item to the head of the linked list
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

    def _add(self, node: 'Node'):
        # Add a node to the head of the linked list
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove(self, node: 'Node'):
        # Remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
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