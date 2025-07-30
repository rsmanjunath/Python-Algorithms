"""
Question: Cloud Jumping

Write a program to calculate the remaining energy of a player after jumping through clouds in a circular array. Each jump costs energy, and landing on a thundercloud costs additional energy.

Input:
- A list `arr` of integers representing the clouds (0 for normal, 1 for thundercloud).
- An integer `jump` representing the jump distance.

Output:
- An integer representing the remaining energy.

Example:
Input: arr = [0, 1, 0, 0, 1, 1], jump = 2
Output: 92
Explanation:
Starting with 100 energy, each jump costs 1 energy. Landing on a thundercloud costs an additional 2 energy.
"""

arr = [1,1, 1, 0, 1, 1, 0, 0, 0, 0]
jump = 2 
energy = 100

for i in range(0,len(arr),jump):
    if arr[i] == 0:
        energy -= 1
    elif arr[i] == 1:
        energy -= 3
print(energy)