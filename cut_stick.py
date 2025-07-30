"""
Question: Cut the Sticks

Write a program to repeatedly cut sticks in an array by the length of the smallest stick until no sticks are left. Return the number of sticks cut in each iteration.

Input:
- A list `arr` of integers representing the lengths of the sticks.

Output:
- A list of integers representing the number of sticks cut in each iteration.

Example:
Input: arr = [5, 1, 2, 3]
Output: [4, 3, 2, 1]
Explanation:
Iteration 1: Cut all sticks by 1 (smallest stick), remaining sticks = [4, 1, 2, 3], count = 4.
Iteration 2: Cut all sticks by 1, remaining sticks = [3, 1, 2], count = 3.
... and so on.
"""

def cutTheSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print(len(arr))
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()
    


sticks = [5,4,4,2,2,8]
print(cutTheSticks(sticks))