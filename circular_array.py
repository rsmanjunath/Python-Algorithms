"""
Question: Circular Array Rotation

Write a program to calculate the new position of elements in an array after a given number of rotations.

Input:
- A list `a` of integers representing the array.
- An integer `k` representing the number of rotations.

Output:
- The new position of elements in the array after `k` rotations.

Example:
Input: a = [1, 2, 3], k = 2
Output: [2, 3, 1]
Explanation:
After 1 rotation: [3, 1, 2]
After 2 rotations: [2, 3, 1]
"""

a = [1,2,3]
k = 2
first = -2 % 5


print(first)
