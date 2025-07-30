"""
Question: Drawing Book

Write a program to determine the minimum number of pages to turn to reach a target page in a book.

Input:
- An integer `n` representing the total number of pages in the book.
- An integer `p` representing the target page.

Output:
- An integer representing the minimum number of pages to turn.

Example:
Input: n = 6, p = 5
Output: 1
Explanation:
From the front: Turn 2 pages to reach page 5.
From the back: Turn 1 page to reach page 5.
Minimum = 1.
"""

def drawing(n,p):
    return min(p//2, n//2 - p//2)


print(drawing(10,10))