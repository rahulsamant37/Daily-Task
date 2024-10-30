# DSA Problem for 2024-10-31

Here is a novel DSA problem with a Python solution for 2024-10-31:

**Problem Statement:**

**Halloween Candy Distribution**

It's Halloween, and you're in charge of distributing candies to trick-or-treaters at a local haunted house. You have a basket full of candies of different types, and each type of candy has a specific score associated with it. The score represents the happiness it brings to the trick-or-treater. You want to distribute the candies in a way that maximizes the total happiness.

The trick-or-treaters will arrive in groups, and each group has a specific size. You can only distribute one type of candy to each group. Your goal is to find the maximum total happiness you can achieve by distributing the candies to the groups.

**Input:**

* `candies`: A list of tuples, where each tuple contains the type of candy and its score. For example: `[(1, 5), (2, 3), (3, 4), ...]`.
* `groups`: A list of integers, where each integer represents the size of a group of trick-or-treaters. For example: `[3, 2, 4, 1, 3]`.

**Output:**

The maximum total happiness you can achieve by distributing the candies to the groups.

**Example:**

```
candies = [(1, 5), (2, 3), (3, 4), (1, 2), (2, 6), (3, 1)]
groups = [3, 2, 4]

Output: 23
```

**Optimal Solution:**
```python
def halloween_candy_distribution(candies, groups):
    # Sort the candies in descending order of their scores
    candies.sort(key=lambda x: x[1], reverse=True)

    # Sort the groups in descending order of their sizes
    groups.sort(reverse=True)

    # Initialize the total happiness
    total_happiness = 0

    # Iterate over the groups and distribute the candies
    for group_size in groups:
        # Find the candy that will bring the maximum happiness to the group
        max_happiness_candy = max(candies[:group_size], key=lambda x: x[1])
        total_happiness += max_happiness_candy[1] * group_size
        # Remove the distributed candies from the basket
        candies = [candy for candy in candies if candy != max_happiness_candy]

    return total_happiness
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n log n) + O(m log m) + O(n*m), where n is the number of candies and m is the number of groups. The first term is for sorting the candies, the second term is for sorting the groups, and the third term is for iterating over the groups and distributing the candies.
* Space complexity: O(1), since we only use a small amount of extra memory to store the sorted lists and the total happiness.

Note: This problem can be solved using dynamic programming, but the above solution is a greedy approach that takes advantage of the fact that the candies and groups can be sorted in a way that maximizes the total happiness.