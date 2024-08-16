# Python Question: Implement a LRU Cache
'''
Implement a Least Recently Used (LRU) cache. It should support the following operations:

*   `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   `put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache(2); // capacity = 2

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
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node() # Dummy head node for the doubly linked list
        self.tail = Node() # Dummy tail node for the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        """
        Add a node to the head of the linked list.
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """
        Remove a node from the linked list.
        """
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev

    def _move_to_head(self, node: Node):
        """
        Move an existing node to the head of the linked list.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the last node (tail) from the linked list.
        """
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key: int) -> int:
        """
        Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)  # Move the node to the head (most recently used)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node) # Move the node to the head (most recently used)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node(node) # Add the node to the head

            if len(self.cache) > self.capacity:
                # Remove the least recently used item
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

    cache2 = LRUCache(1)
    cache2.put(2,1)
    assert cache2.get(2) == 1
    cache2.put(3,2)
    assert cache2.get(2) == -1
    assert cache2.get(3) == 2

    cache3 = LRUCache(2)
    cache3.put(2, 1)
    cache3.put(1, 1)
    cache3.put(2, 3)
    cache3.put(4, 1)
    assert cache3.get(1) == -1
    assert cache3.get(2) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()