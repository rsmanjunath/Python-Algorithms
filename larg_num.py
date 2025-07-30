"""
Question: Largest Number

Write a program to form the largest number possible from a list of non-negative integers.

Input:
- A list `nums` of non-negative integers.

Output:
- A string representing the largest number that can be formed.

Example:
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
Explanation:
The largest number formed by arranging the integers is "9534330".
"""

s = [78,890,678,6778,45]
a = [str(i) for i in s]

for i in range(len(a)-1):

    for j in range(i+1, len(a)):
        if a[i]+a[j] < a[j]+a[i]:
            a[i], a[j] = a[j], a[i]
            
print("".join(a))