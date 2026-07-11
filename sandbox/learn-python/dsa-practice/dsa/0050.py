# DSA Problem 50

'''
Problem Statement:
A group of n friends are planning to share a secret. They decide to use a method where each friend will share the secret with exactly two other friends, but no friend can share the secret with someone who has already received it from another friend. Also, a friend cannot share the secret with themselves.

Write a function `can_share_secret(n)` that returns "Yes" if it is possible for all n friends to share the secret according to these rules, and "No" otherwise.

For example:
- If there are 3 friends, one possible way for them to share the secret is Friend 1 shares with Friend 2 and Friend 3, Friend 2 shares with Friend 3 and Friend 1, and Friend 3 shares with Friend 1 and Friend 2. Hence `can_share_secret(3)` should return "Yes".
- If there are 4 friends, it's not possible for each friend to share the secret with exactly two others without breaking the rules. Hence `can_share_secret(4)` should return "No".
'''

Solution:
```python
def can_share_secret(n):
    """
    Determines if it's possible for n friends to share a secret such that each friend shares
    the secret with exactly two others, without any friend receiving the secret from more than
    one friend and without a friend sharing the secret with themselves.
    """
    if n <= 1:
        return "No"
    if n % 2 == 0:
        return "No"
    else:
        return "Yes"

# Test the function with sample inputs
print(can_share_secret(3))  # Should return "Yes"
print(can_share_secret(4))  # Should return "No"
print(can_share_secret(5))  # Should return "Yes"
```

Explanation:
The solution checks if the number of friends `n` is less than or equal to 1 or if `n` is an even number. If either condition is met, it's not possible for each friend to share the secret with exactly two others without breaking the given rules. Therefore, for a valid sharing circle to form, `n` must be an odd number greater than 1, allowing a cyclic sharing pattern among the friends.