# DSA Problem for 2024-12-20

Here is a novel DSA problem with a Python solution for 2024-12-20:

**Problem Statement:**

**"Santa's Gift Factory"**

Santa's gift factory is getting ready for the holiday season, and they need your help to optimize their gift wrapping process. They have a list of gifts to wrap, each with a unique wrapping paper design and a specific number of gifts to wrap. The wrapping paper designs are represented as strings, and each design has a unique prefix and suffix.

The factory has a limited number of wrapping paper rolls, each with a fixed capacity. The goal is to wrap as many gifts as possible using the available wrapping paper rolls.

Write a function `wrap_gifts(gifts, paper_rolls)` that takes in two inputs:

* `gifts`: a list of tuples, where each tuple contains the wrapping paper design (string) and the number of gifts to wrap (integer)
* `paper_rolls`: a list of integers, where each integer represents the capacity of a wrapping paper roll

The function should return the maximum number of gifts that can be wrapped using the available wrapping paper rolls.

**Optimal Solution:**

```
def wrap_gifts(gifts, paper_rolls):
    # Sort gifts by wrapping paper design length in descending order
    gifts.sort(key=lambda x: len(x[0]), reverse=True)

    # Sort paper rolls by capacity in descending order
    paper_rolls.sort(reverse=True)

    wrapped_gifts = 0
    paper_roll_idx = 0

    for gift in gifts:
        while paper_roll_idx < len(paper_rolls) and paper_rolls[paper_roll_idx] < len(gift[0]):
            paper_roll_idx += 1

        if paper_roll_idx < len(paper_rolls):
            paper_rolls[paper_roll_idx] -= len(gift[0])
            wrapped_gifts += gift[1]

    return wrapped_gifts
```

**Time/Space Complexity Analysis:**

* Time complexity: O(n log n + m log m) where n is the number of gifts and m is the number of paper rolls. The sorting operations dominate the time complexity.
* Space complexity: O(1) since we only use a few extra variables to store the sorted lists and the result.

**Explanation:**

The solution first sorts the gifts by wrapping paper design length in descending order, so that we can try to wrap the gifts with the longest designs first. Then, it sorts the paper rolls by capacity in descending order, so that we can use the largest paper rolls first.

The solution then iterates through the gifts, and for each gift, it tries to find a paper roll that can accommodate the wrapping paper design. If a suitable paper roll is found, it wraps the gift and updates the remaining capacity of the paper roll. The process continues until all gifts are processed or all paper rolls are used up.

The solution has an optimal time and space complexity because it uses sorting to reduce the number of iterations and avoids unnecessary computations by skipping paper rolls that are too small to accommodate the wrapping paper design.