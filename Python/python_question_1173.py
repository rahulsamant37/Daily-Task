# Python Question: Implement a Circular Buffer
'''
Implement a circular buffer (also known as a ring buffer). A circular buffer is a fixed-size buffer that operates as if it were connected end-to-end, allowing data to be written and read in a circular fashion.

Your task is to implement a `CircularBuffer` class with the following methods:

*   `__init__(self, capacity)`: Initializes the buffer with a given capacity.
*   `is_empty(self)`: Returns `True` if the buffer is empty, `False` otherwise.
*   `is_full(self)`: Returns `True` if the buffer is full, `False` otherwise.
*   `enqueue(self, item)`: Adds an item to the rear of the buffer. If the buffer is full, overwrite the oldest element (the element at the front).
*   `dequeue(self)`: Removes and returns the item at the front of the buffer. If the buffer is empty, return `None`.
*   `peek(self)`: Returns the item at the front of the buffer without removing it. If the buffer is empty, return `None`.
*   `size(self)`: Returns the number of elements currently in the buffer.

Example: