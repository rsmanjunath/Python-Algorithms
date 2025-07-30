"""
Question: Gemstones

Write a program to determine the number of gemstones in a list of rocks. A gemstone is an element that appears in each rock.

Input:
- A list `rocks` of strings representing the composition of each rock.

Output:
- An integer representing the number of gemstones.

Example:
Input: rocks = ["abcdde", "baccd", "eeabg"]
Output: 2
Explanation:
The elements 'a' and 'b' appear in all three rocks.
"""

n = int(input())
first_input = set(input())

for i in range(n-1):
    rest_input = set(input())
    first_input = first_input & rest_input

print(len(first_input))