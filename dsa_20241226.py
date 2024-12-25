# DSA Problem for 2024-12-26

Here is a novel DSA problem with a Python solution:

**Problem Statement:**

**"Snowflake Sorting"**

It's Christmas time, and Santa Claus is preparing for the big night! He has a bag of magical snowflakes, each with a unique shape and size. However, the snowflakes are all jumbled up in the bag, and Santa needs to sort them out quickly.

The snowflakes can be represented as a list of integers, where each integer corresponds to the diameter of a snowflake. Santa wants to sort the snowflakes in a specific order: he wants to group all snowflakes with diameters that are multiples of 3 together, followed by snowflakes with diameters that are multiples of 2 but not 3, and finally, the remaining snowflakes.

For example, given the list `[12, 4, 9, 15, 6, 24, 3, 8, 10]`, the sorted list should be `[12, 24, 6, 3, 9, 15, 4, 8, 10]`.

**Optimal Solution:**

Here is a Python solution that uses a single pass through the input list:
```python
def snowflake_sorting(snowflakes):
    multiples_of_3 = []
    multiples_of_2_not_3 = []
    remaining = []

    for snowflake in snowflakes:
        if snowflake % 3 == 0:
            multiples_of_3.append(snowflake)
        elif snowflake % 2 == 0:
            multiples_of_2_not_3.append(snowflake)
        else:
            remaining.append(snowflake)

    return multiples_of_3 + multiples_of_2_not_3 + remaining
```
**Time/Space Complexity Analysis:**

* **Time Complexity:** O(n), where n is the length of the input list. We only iterate through the input list once, and the operations inside the loop are constant time.
* **Space Complexity:** O(n), since we create three additional lists to store the sorted snowflakes. In the worst case, all snowflakes could end up in one of these lists, so the space complexity is linear.

Note that this solution has a linear time complexity, which is optimal for this problem. We can't do better than O(n) because we need to examine each snowflake at least once to determine its category.

Hope you enjoy this festive DSA problem!