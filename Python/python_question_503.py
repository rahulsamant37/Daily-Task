# Python Question: Implement a LRU Cache
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

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
class LRUCache:

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.
        We use a doubly linked list to maintain the order of usage and a dictionary
        to store the key-value pairs. This allows O(1) get and put operations.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        """
        Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
        If the key exists, move the node to the head of the list (most recently used).
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Set or insert the value if the key is not already present.
        When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node(node)
            self.size += 1

            if self.size > self.capacity:
                # Remove the tail node (least recently used)
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

    def _add_node(self, node):
        """
        Add a node to the head of the linked list.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove a node from the linked list.
        """
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    def _move_to_head(self, node):
        """
        Move an existing node to the head of the list.
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


class Node:
    """
    Helper class for the doubly linked list.
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
    cache.put(2,1)
    assert cache.get(2) == 1
    cache.put(3,2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2

    cache = LRUCache(2)
    cache.get(2)
    cache.put(2,6)
    cache.get(1)
    cache.put(1,5)
    cache.put(1,2)
    cache.get(1)
    cache.get(2)
    print("All test cases passed")


if __name__ == "__main__":
    test_solution()