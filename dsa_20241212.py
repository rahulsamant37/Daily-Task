# DSA Problem for 2024-12-12

**Problem Statement:**

**Santa's Gift Sleigh Scheduling**

It's Christmas Eve, and Santa needs your help to schedule his gift delivery. He has a list of gifts to deliver to children all around the world, and each gift has a specific deadline to be delivered. Additionally, each gift requires a certain amount of time to be loaded onto the sleigh. Santa wants to minimize the total time spent loading gifts onto the sleigh.

You are given a list of gifts, where each gift is represented by a tuple `(deadline, load_time)`. The `deadline` is the time by which the gift must be delivered, and the `load_time` is the time it takes to load the gift onto the sleigh.

Write a function `schedule_gifts(gifts)` that returns the minimum total time spent loading gifts onto the sleigh, such that all gifts are delivered on time.

**Optimal Solution:**
```python
def schedule_gifts(gifts):
    gifts.sort(key=lambda x: x[0])  # sort by deadline
    total_load_time = 0
    current_time = 0

    for deadline, load_time in gifts:
        current_time += load_time
        if current_time > deadline:
            return -1  # impossible to deliver all gifts on time
        total_load_time += load_time

    return total_load_time
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n log n), where n is the number of gifts. This is because we sort the list of gifts by deadline, which takes O(n log n) time using the built-in `sort` function. The subsequent iteration over the sorted list takes O(n) time.

**Space Complexity Analysis:**

The space complexity of this solution is O(1), since we only use a small amount of extra memory to store the `total_load_time` and `current_time` variables.

**Explanation:**

The key insight to this problem is to sort the gifts by deadline. By doing so, we can ensure that we load the gifts onto the sleigh in the order of their deadlines. This allows us to minimize the total time spent loading gifts, since we can load gifts with earlier deadlines first.

We iterate over the sorted list of gifts, and for each gift, we add its load time to the current time. If the current time exceeds the deadline for the current gift, we return -1, indicating that it's impossible to deliver all gifts on time.

Finally, we return the total load time, which is the minimum time spent loading gifts onto the sleigh.

I hope you enjoy solving this problem!