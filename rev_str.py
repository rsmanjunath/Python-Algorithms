"""
Question: Reverse String

Write a program to reverse a given string.

Input:
- A string `s` representing the string to reverse.

Output:
- A string representing the reversed string.

Example:
Input: s = "hello"
Output: "olleh"
Explanation:
The reverse of "hello" is "olleh".
"""

s = "Manjunath" 
str = "" 
for i in s: 
    str = i + str
    print(str)
print(str)
