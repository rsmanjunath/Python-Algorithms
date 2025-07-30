"""
Question: Halloween Sale

Write a program to calculate the maximum number of items that can be purchased during a sale, given the initial price, discount, and minimum price.

Input:
- An integer `p` representing the initial price of an item.
- An integer `d` representing the discount per item.
- An integer `m` representing the minimum price of an item.
- An integer `s` representing the total budget.

Output:
- An integer representing the maximum number of items that can be purchased.

Example:
Input: p = 20, d = 3, m = 6, s = 80
Output: 6
Explanation:
Items purchased: 20, 17, 14, 11, 8, 6 (total = 76, within budget).
"""

p = 20
d = 3
m = 6
s = 85

count = 0
while s>=p:
    count += 1
    s = s-p
    p = max(p-d,m)

print(count)