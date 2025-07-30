"""
Question: Alternating Matrix Traversal

Write a program to traverse a 2D matrix in an alternating left-to-right and right-to-left order for each row.

Input:
- A 2D matrix `n` of integers.

Output:
- Elements of the matrix printed in the specified traversal order.

Example:
Input: n = [[1,2,3],[4,5,6],[7,8,9]]
Output: 1 2 3 6 5 4 7 8 9
Explanation:
Row 1: Left-to-right -> 1 2 3
Row 2: Right-to-left -> 6 5 4
Row 3: Left-to-right -> 7 8 9
"""

n = [[1,2,3],[4,5,6],[7,8,9]]
left_to_right = True
for i in range(len(n)):
    if (left_to_right):
        for j in range(len(n)):
            print(n[i][j],end = " ")
    else:
        for j in range(len(n)-1,-1,-1):
            print(n[i][j],end = " ")
    left_to_right = not left_to_right