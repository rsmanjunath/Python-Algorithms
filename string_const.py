"""
Question: Count Unique Characters

Write a program to count the number of unique characters in a given string.

Input:
- A string `s` consisting of lowercase English letters.

Output:
- An integer representing the count of unique characters in the string.

Example:
Input: s = "abab"
Output: 2
Explanation:
The unique characters in the string "abab" are 'a' and 'b', so the count is 2.
"""

s = "abab"
count = 0

orig = ""
for i in s:
    if i not in orig:
        orig += i
        count += 1

print(count)
