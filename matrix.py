"""
Question: Matrix Manipulation

Write a program to perform specific operations on a 2D matrix, such as rotation, transposition, or flipping.

Input:
- A 2D list `matrix` representing the matrix.
- A string `operation` representing the operation to perform (e.g., "rotate", "transpose").

Output:
- A 2D list representing the modified matrix.

Example:
Input: matrix = [[1, 2], [3, 4]], operation = "rotate"
Output: [[3, 1], [4, 2]]
Explanation:
The matrix is rotated 90 degrees clockwise.
"""

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = 3
n = 3
row_start = 0
row_end = m - 1
col_start = 0
col_end = n - 1
while row_start <= row_end and col_start <= col_end:


    for i in range(col_start, col_end + 1):
        print(arr[row_start][i])
    row_start += 1

    for i in range(row_start, row_end + 1):
        print(arr[i][col_end])
    col_end -= 1

    for i in range(col_end, col_start-1, -1):
        print(arr[row_end][i])
    row_end -= 1

    for i in range(row_end,row_start-1,-1):
        print(arr[i][col_start])
    col_start += 1