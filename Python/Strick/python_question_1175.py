# Python Question: Implement a LRU Cache
'''
Implement a Least Recently Used (LRU) cache. It should support the following operations:

*   `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   `put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

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
        Initializes the LRU cache with the given capacity.
        Uses a dictionary to store key-value pairs and a doubly linked list to maintain the order of access.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.head = Node(0, 0)  # Dummy head node of the linked list
        self.tail = Node(0, 0)  # Dummy tail node of the linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # Current size of the cache

    def get(self, key: int) -> int:
        """
        Gets the value of the key if the key exists in the cache, otherwise returns -1.
        Moves the accessed node to the head of the linked list.
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
            node.value = value
            self._move_to_head(node)  # Update the value and move to head
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node(node)  # Add the new node to the head
            self.size += 1

            if self.size > self.capacity:
                # Evict the least recently used node (tail.prev)
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
                self.size -= 1

    def _add_node(self, node):
        """
        Adds a node to the head of the linked list.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Removes a node from the linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """
        Moves a node to the head of the linked list.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pops the tail node (least recently used) from the linked list.
        """
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node


class Node:
    """
    Represents a node in the doubly linked list.
    Each node stores a key, value, and pointers to the previous and next nodes.
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

    cache2 = LRUCache(1)
    cache2.put(2, 1)
    assert cache2.get(2) == 1
    cache2.put(3, 2)
    assert cache2.get(2) == -1
    assert cache2.get(3) == 2

    cache3 = LRUCache(3)
    cache3.put(1,1)
    cache3.put(2,2)
    cache3.put(3,3)
    cache3.put(4,4)
    assert cache3.get(4) == 4
    assert cache3.get(3) == 3
    assert cache3.get(2) == 2
    assert cache3.get(1) == -1
    cache3.put(5,5)
    assert cache3.get(1) == -1
    assert cache3.get(2) == 2
    assert cache3.get(3) == 3
    assert cache3.get(4) == -1
    assert cache3.get(5) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()