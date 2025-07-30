"""
Question: Hurdle Race

Write a program to determine the minimum number of doses a character needs to jump over the tallest hurdle.

Input:
- A list `hurdles` of integers representing the heights of hurdles.
- An integer `k` representing the maximum height the character can jump naturally.

Output:
- An integer representing the minimum number of doses required.

Example:
Input: hurdles = [1, 2, 3, 3, 2], k = 1
Output: 2
Explanation:
The tallest hurdle is 3. The character can jump 1 naturally, so 2 doses are needed to jump 3.
"""

height = [2 ,5 ,4 ,5 ,2]
k = 7
if k >= max(height):
    print(0)
else:
    print(max(height) - k)