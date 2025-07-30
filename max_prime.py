"""
Question: Maximum Prime Factor

Write a program to find the largest prime factor of a given number.

Input:
- An integer `n` representing the number.

Output:
- An integer representing the largest prime factor of `n`.

Example:
Input: n = 13195
Output: 29
Explanation:
The prime factors of 13195 are 5, 7, 13, and 29. The largest is 29.
"""

def max_factor(num):
    """Find the maximum prime factor."""
    best = None
    factor = 2 
    while factor * factor <= num:
        while num % factor == 0:
            best = factor
            num /= factor
        factor += 1
    if (num > 1): 
        return num 
    return best