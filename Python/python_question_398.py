# Python Question: Implement a LRU Cache
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

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
class LRUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.usage_list = []  # List to maintain the order of usage (most recently used at the end)

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Move the key to the end of the usage list (mark as recently used)
            self.usage_list.remove(key)
            self.usage_list.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Update the value and move the key to the end of the usage list
            self.cache[key] = value
            self.usage_list.remove(key)
            self.usage_list.append(key)
        else:
            if len(self.cache) == self.capacity:
                # Remove the least recently used item (first element in the usage list)
                lru_key = self.usage_list.pop(0)
                del self.cache[lru_key]

            # Add the new key-value pair to the cache and usage list
            self.cache[key] = value
            self.usage_list.append(key)

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
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.put(4,1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()