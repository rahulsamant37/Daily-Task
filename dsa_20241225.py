# DSA Problem for 2024-12-25

Here is a novel DSA problem with a Python solution for 2024-12-25:

**Problem Statement:**

**Christmas Tree Decoration**

It's Christmas Eve, and you're in charge of decorating the city's giant Christmas tree. The tree has `n` levels, and each level can hold `m` ornaments of different colors. You have a set of ornaments with different colors, and each ornament has a unique ID.

Your goal is to decorate the tree such that each level has exactly `m` ornaments, and no two ornaments of the same color are placed on the same level. You also want to minimize the total number of different colors used on the tree.

Write a Python function `decorate_tree(ornaments, n, m)` that takes as input a list of ornaments `ornaments`, where each ornament is represented as a tuple `(id, color)`, and the tree's dimensions `n` and `m`. The function should return a list of lists, where each inner list represents the ornaments on a level of the tree, satisfying the conditions above.

**Optimal Solution:**
```
from collections import defaultdict

def decorate_tree(ornaments, n, m):
    # Create a dictionary to store ornaments by color
    ornaments_by_color = defaultdict(list)
    for ornament in ornaments:
        ornaments_by_color[ornament[1]].append(ornament)

    # Create a list to store the decorated tree
    decorated_tree = []

    # Iterate over the levels of the tree
    for _ in range(n):
        # Create a list to store the ornaments on this level
        level_ornaments = []

        # Iterate over the colors, and try to place an ornament of each color
        for color in ornaments_by_color:
            if ornaments_by_color[color]:
                ornament = ornaments_by_color[color].pop(0)
                level_ornaments.append(ornament)

        # If we didn't find enough ornaments, return an empty list
        if len(level_ornaments) < m:
            return []

        # Add the level to the decorated tree
        decorated_tree.append(level_ornaments)

    return decorated_tree
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n \* m), where `n` is the number of levels and `m` is the number of ornaments per level. This is because we iterate over the levels of the tree, and for each level, we iterate over the colors and try to place an ornament of each color.
* Space complexity: O(n \* m), where `n` is the number of levels and `m` is the number of ornaments per level. This is because we store the decorated tree, which has `n` levels, each with `m` ornaments.

Note that the solution assumes that there are enough ornaments of different colors to decorate the tree. If there are not enough ornaments, the function returns an empty list.