"""
Question: Mouse and Cheese

Write a program to calculate the maximum amount of cheese a mouse can collect in a grid. The mouse can only move right or down.

Input:
- A 2D list `grid` representing the grid of integers where each cell contains the amount of cheese.

Output:
- An integer representing the maximum amount of cheese the mouse can collect.

Example:
Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: 21
Explanation:
The path 1 → 4 → 7 → 8 → 9 collects the maximum cheese of 21.
"""

def mouse(x,y,z):
    f = abs(z - x)
    s = abs(z - y)
    if f > s:
        return "CAT B"
    elif s > f:
        return "CAT A"
    else:
        return "MOUSE C"

print(mouse(1,3,2))