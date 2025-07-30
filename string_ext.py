"""
Question: Infinite String Extension

Write a program to extend a given string `s` infinitely until a specified length `n` is reached.

Input:
- A string `s` consisting of lowercase English letters.
- An integer `n` representing the desired length of the extended string.

Output:
- A string representing the extended version of `s` repeated until length `n`.

Example:
Input: s = "aabbaabaa", n = 20
Output: "aabbaabaaabbaabaaab"
Explanation:
The string "aabbaabaa" is repeated to reach the desired length of 20 characters.
"""

s = "aabbaabaa"
n = 20
str1 = " "
while n > 0:
    k = n
    for i in range(len(s)):
        str1 += s[i]
        
    k -= 1

print(str1)




