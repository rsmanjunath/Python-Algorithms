"""
Question: Knapsack Problem

Write a program to solve the 0/1 Knapsack problem, where you maximize the total value of items that can be carried in a knapsack of limited capacity.

Input:
- A list `weights` of integers representing the weights of items.
- A list `values` of integers representing the values of items.
- An integer `capacity` representing the maximum weight the knapsack can carry.

Output:
- An integer representing the maximum total value that can be carried.

Example:
Input: weights = [1, 2, 3], values = [6, 10, 12], capacity = 5
Output: 22
Explanation:
Select items with weights 2 and 3 for a total value of 10 + 12 = 22.
"""

arr[n][c] = []

def knap(n,c):
    if arr[n][c] != []:
        return arr[n][c]
    if n == 0 or c == 0:
        result = 0
    elif weight[n] > c:
        result = knap(n-1,c)
    else:
        temp1 = knap(n-1,c)
        temp2 = value[n] + knap(n-1,c-weight[n])
        result = max(temp1,temp2)
    return result

weight = [1,2,4,2,5]
value = [5,3,5,3,2]
n = len(weight)
c = 10
print(knap(4,10))


