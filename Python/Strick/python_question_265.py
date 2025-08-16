# Python Question: Implement a Custom LRU Cache
'''
Implement a Least Recently Used (LRU) cache with a fixed capacity. The cache should support the following operations:

*   `get(key)`: Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
*   `put(key, value)`: Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The LRU cache should be implemented using a doubly linked list and a hash map (dictionary). The doubly linked list will maintain the order of the keys based on their usage, with the most recently used key at the head and the least recently used key at the tail. The hash map will store the key-value pairs and pointers to the corresponding nodes in the doubly linked list.

Example: