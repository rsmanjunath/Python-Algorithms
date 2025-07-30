"""
Question: Library Fine

Write a program to calculate the fine for returning a library book late. The fine is calculated based on the number of days, months, and years late.

Input:
- Three integers `d1`, `m1`, `y1` representing the return date.
- Three integers `d2`, `m2`, `y2` representing the due date.

Output:
- An integer representing the fine.

Example:
Input: d1 = 9, m1 = 6, y1 = 2015, d2 = 6, m2 = 6, y2 = 2015
Output: 45
Explanation:
The book is 3 days late, so the fine is 3 * 15 = 45.
"""

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        return 0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    elif m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    else:
        return 10000


d1 = 9
d2 = 7
m1 = 4
m2 = 4
y1 = 5
y2 = y1

print(libraryFine(d1, m1, y1, d2, m2, y2))
