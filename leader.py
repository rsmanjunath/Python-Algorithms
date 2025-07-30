"""
Question: Leader in an Array

Write a program to find all leaders in an array. An element is a leader if it is greater than all the elements to its right.

Input:
- A list `arr` of integers representing the array.

Output:
- A list of integers representing the leaders in the array.

Example:
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation:
17 is greater than all elements to its right, 5 is greater than all elements to its right, and 2 is the last element.
"""

score = [10,20,40,50,100]
alice = [5,25,50,120]
index = 0
rank_list = []
n = len(score)
r = [5,4,3,2,1]
for i in alice:
    if i >= score[index]:
        rank_list.append(r[index] - 1)
        index += 1
    else:
        rank_list.append(r[index] + 1)
        index += 1

print(rank_list)