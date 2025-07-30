"""
Question: Beautiful Days at the Movies

Write a program to count the number of "beautiful days" in a given range. A day is considered beautiful if the absolute difference between the day and its reverse is divisible by a given number `k`.

Input:
- Two integers `i` and `j` representing the range of days.
- An integer `k` representing the divisor.

Output:
- An integer representing the count of beautiful days.

Example:
Input: i = 20, j = 23, k = 6
Output: 2
Explanation:
Day 20: Reverse is 02, |20 - 02| = 18, 18 % 6 == 0 (Beautiful)
Day 21: Reverse is 12, |21 - 12| = 9, 9 % 6 != 0 (Not Beautiful)
Day 22: Reverse is 22, |22 - 22| = 0, 0 % 6 == 0 (Beautiful)
Day 23: Reverse is 32, |23 - 32| = 9, 9 % 6 != 0 (Not Beautiful)
"""

i = 20
j = 23
k = 6
count = 0
for num in range(i, j+1):
    n = (str(num)[::-1])
    if abs(int(n) - num) % k == 0:
        count += 1
print(count)

