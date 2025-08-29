class Node:
    """
    Without __future__, you would need string quotes to avoid NameError:
    """
    def __init__(self, value: int, next: 'Node' = None):  # Forward reference in quotes
        self.value = value
        self.next = next

from __future__ import annotations

class Node:
    def __init__(self, value: int, next: Node = None):  # No need for quotes
        self.value = value
        self.next = next
