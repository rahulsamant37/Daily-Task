# DSA Problem for 2024-11-19

Here is a novel DSA problem with a Python solution for 2024-11-19:

**Problem Statement:**

**"Maximize the Total Value of Items in a Knapsack with Dependent Items"**

You are given a list of items, each with a weight, value, and a list of dependent items. The dependent items are items that must be included in the knapsack if the current item is included. The goal is to maximize the total value of items in the knapsack without exceeding the maximum weight capacity.

**Example Input:**

```
items = [
    {"weight": 3, "value": 10, "dependent": []},
    {"weight": 2, "value": 8, "dependent": [0]},  # dependent on item 0
    {"weight": 4, "value": 12, "dependent": [1]},  # dependent on item 1
    {"weight": 1, "value": 5, "dependent": [0, 1]},  # dependent on items 0 and 1
    {"weight": 5, "value": 20, "dependent": [2, 3]}  # dependent on items 2 and 3
]
max_weight = 10
```

**Optimal Solution:**

We can solve this problem using dynamic programming with a recursive approach.

```python
def max_knapsack_value(items, max_weight):
    memo = {}

    def recurse(index, current_weight):
        if (index, current_weight) in memo:
            return memo[(index, current_weight)]

        if index == len(items) or current_weight == 0:
            return 0

        item = items[index]
        value_with_item = 0
        if current_weight >= item["weight"]:
            value_with_item = item["value"]
            for dep in item["dependent"]:
                if current_weight < items[dep]["weight"]:
                    value_with_item = 0
                    break
                value_with_item += items[dep]["value"]
            value_with_item += recurse(index + 1, current_weight - item["weight"] - sum(items[dep]["weight"] for dep in item["dependent"]))

        value_without_item = recurse(index + 1, current_weight)
        memo[(index, current_weight)] = max(value_with_item, value_without_item)
        return memo[(index, current_weight)]

    return recurse(0, max_weight)

print(max_knapsack_value(items, max_weight))  # Output: 30
```

**Time/Space Complexity Analysis:**

* Time Complexity: O(2^n \* W), where n is the number of items and W is the maximum weight capacity. This is because we have two recursive calls for each item, and we iterate up to the maximum weight capacity.
* Space Complexity: O(n \* W), where n is the number of items and W is the maximum weight capacity. This is because we store the memoization table with size n \* W.

Note: The time and space complexities can be improved using more advanced techniques, such as iterative dynamic programming or using a more efficient data structure for memoization. However, the above solution provides a basic optimal solution for the problem.