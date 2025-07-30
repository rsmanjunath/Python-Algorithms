"""
Question: Picking Numbers

Write a program to find the maximum number of integers you can select from an array such that the absolute difference between any two of the selected integers is less than or equal to 1.

Input:
- A list `arr` of integers representing the array.

Output:
- An integer representing the maximum number of integers that can be selected.

Example:
Input: arr = [4, 6, 5, 3, 3, 1]
Output: 3
Explanation:
The subarray [4, 3, 3] satisfies the condition.
"""

arr = [1,1,2,2,4,4,5,5,5]
res = []

maximum = 0
diff = 1

for k in arr:
    n1 = arr.count(k)
    n2 = arr.count(k-diff) #find number of respective values with given difference.
    maximum = max(maximum, n1+n2)

print(maximum)







