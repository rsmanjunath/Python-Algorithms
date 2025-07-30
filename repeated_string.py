"""
Question: Repeated String

Write a program to find the number of occurrences of a character in the first `n` characters of an infinitely repeated string.

Input:
- A string `s` representing the base string.
- An integer `n` representing the number of characters to consider.

Output:
- An integer representing the number of occurrences of the character 'a'.

Example:
Input: s = "abcac", n = 10
Output: 4
Explanation:
The first 10 characters of the infinitely repeated string are "abcacabcac". The character 'a' appears 4 times.
"""

s = "aba"
n = 10

new_s = ""

while n > 0:
    for i in range(len(s)):
        new_s += s[i]
        if len(new_s) == 10:
            break
        else:
            n -= 1
print(new_s)
