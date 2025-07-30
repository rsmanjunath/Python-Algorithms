"""
Question: Viral Advertising

HackerLand Enterprise is launching a new advertising campaign. On the first day, the company delivers the advertisement to `rece` people. 
Each person who receives the advertisement shares it with 3 of their friends on the next day. 
Assume that only half of the people who receive the advertisement actually like it and will share it further.

Given `n` days, calculate the cumulative number of people who have liked the advertisement by the end of the campaign.

Input:
- An integer `n` representing the number of days the advertisement campaign runs.

Output:
- An integer representing the cumulative number of likes.

Example:
Input: n = 3
Output: 9
Explanation:
Day 1: 5 people receive the ad, 2 like it (5 // 2), and 2 * 3 = 6 people receive it the next day.
Day 2: 6 people receive the ad, 3 like it (6 // 2), and 3 * 3 = 9 people receive it the next day.
Day 3: 9 people receive the ad, 4 like it (9 // 2).
Cumulative likes = 2 + 3 + 4 = 9.
"""

n = 3
likes = 0
rece = 5
cumu = 0
for i in range(0, n):
    likes = rece // 2
    cumu += likes
    rece = likes * 3

print(cumu)
