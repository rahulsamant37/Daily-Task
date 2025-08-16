# Python Question: Implement a LRU Cache
'''
Implement a Least Recently Used (LRU) cache with the following operations:

*   `LRUCache(capacity: int)`: Initialize the cache with a positive capacity.
*   `get(key: int) -> int`: Return the value of the key if the key exists in the cache, otherwise return -1.
*   `put(key: int, value: int) -> None`: Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The `get` and `put` operations must both run in O(1) average time complexity.

Example: