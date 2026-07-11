# Python Question: Implement a LRU Cache
'''
Implement a Least Recently Used (LRU) cache. It should support the following operations:

*   `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   `put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

The `get` and `put` operations must both run in O(1) time.

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
        """
        Initializes the LRU cache with the given capacity.
        Uses a doubly linked list to keep track of the order of recently used items.
        Uses a dictionary to map keys to nodes in the doubly linked list.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the given key.
        Moves the accessed node to the head of the linked list to mark it as recently used.
        Returns -1 if the key is not found.
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)  # Move the node to the head
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the value associated with the given key.
        If the key exists, updates the value and moves the node to the head.
        If the key doesn't exist, inserts a new node at the head.
        If the cache is full, removes the least recently used node (tail).
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value  # Update the value
            self._move_to_head(node)  # Move the node to the head
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node  # Add to the cache
            self._add_node(new_node)  # Add to the head of the linked list
            self.size += 1

            if self.size > self.capacity:
                # Remove the least recently used node (tail)
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]  # Remove from the cache
                self.size -= 1

    def _add_node(self, node):
        """
        Helper function to add a node to the head of the linked list.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Helper function to remove a node from the linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        """
        Helper function to move a node to the head of the linked list.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Helper function to remove the tail node (least recently used) from the linked list.
        """
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node


class Node:
    """
    Represents a node in the doubly linked list.
    Each node stores a key, a value, and pointers to the previous and next nodes.
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