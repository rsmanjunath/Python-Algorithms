"""
Question: Factorial Calculation

Write a program to calculate the factorial of a given number `n`.

Input:
- An integer `n` representing the number to calculate the factorial for.

Output:
- An integer representing the factorial of `n`.

Example:
Input: n = 5
Output: 120
Explanation:
5! = 5 * 4 * 3 * 2 * 1 = 120
"""

n = 30
fact = 1
for i in range(1,n + 1):
    fact *= i
print(fact)
