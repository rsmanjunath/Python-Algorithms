"""
Question: Equalize the Array

Write a program to determine the minimum number of deletions required to make all elements in an array equal.

Input:
- A list `arr` of integers representing the array.

Output:
- An integer representing the minimum number of deletions required.

Example:
Input: arr = [3, 3, 2, 1, 3]
Output: 2
Explanation:
The most frequent element is 3 (appears 3 times). To make all elements equal to 3, delete 2 elements (2 and 1).
"""

arr = [1,1,1,1,1,2,2,4,5,6,7,8]
c = {}
for i in arr:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1
max_val=max(c, key=c.get)

print(len(arr) - c[max_val])
print(c)
