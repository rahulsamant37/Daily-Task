# DSA Problem for 2024-12-23

Here's a novel DSA problem for 2024-12-23:

**Problem Statement:**

"Santa's Gift Wrapping"

Santa has a list of gifts to wrap for Christmas. Each gift has a unique wrapping paper requirement, which is represented by an integer. Santa has a limited number of wrapping papers, each with a unique pattern, and each pattern can be used to wrap multiple gifts. The wrapping paper requirement of a gift can be satisfied by any wrapping paper that is greater than or equal to the requirement. For example, if a gift requires a wrapping paper of 3, any wrapping paper with a pattern of 3, 4, 5, or higher can be used to wrap it.

Given the list of gift wrapping paper requirements and the available wrapping papers, write a function to determine the minimum number of wrapping papers needed to wrap all gifts.

**Input:**

* `gifts`: a list of integers representing the wrapping paper requirements of each gift
* `papers`: a list of integers representing the available wrapping papers

**Output:**

* The minimum number of wrapping papers needed to wrap all gifts

**Example:**

```
gifts = [3, 2, 4, 1, 5]
papers = [2, 3, 5, 7]
output: 3
```

In this example, the gifts require wrapping papers of 3, 2, 4, 1, and 5, respectively. The available wrapping papers are 2, 3, 5, and 7. The minimum number of wrapping papers needed is 3: one paper of 3 can wrap gifts with requirements 1, 2, and 3; one paper of 5 can wrap the gift with requirement 4; and one paper of 5 can wrap the gift with requirement 5.

**Optimal Solution:**
```
def min_wrapping_papers(gifts, papers):
    gifts.sort()
    papers.sort()
    i, j, papers_needed = 0, 0, 0
    while i < len(gifts):
        if j < len(papers) and papers[j] >= gifts[i]:
            papers_needed += 1
            i += 1
            while i < len(gifts) and papers[j] >= gifts[i]:
                i += 1
        j += 1
    return papers_needed
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n log n + m log m), where n is the number of gifts and m is the number of wrapping papers. This is because we sort the gifts and papers lists, which takes O(n log n) and O(m log m) time, respectively. The while loop iterates at most n times, and the inner while loop iterates at most n times in the worst case. Therefore, the overall time complexity is dominated by the sorting operations.

**Space Complexity Analysis:**

The space complexity of the solution is O(1), since we only use a few extra variables to store the indices and the result. We do not use any additional data structures that scale with the input size.