"""
Question: Digit Frequency

Write a program to count the frequency of each digit in a given number.

Input:
- An integer `num` representing the number.

Output:
- A dictionary where keys are digits and values are their frequencies.

Example:
Input: num = 112233
Output: {1: 2, 2: 2, 3: 2}
Explanation:
The digit 1 appears 2 times, 2 appears 2 times, and 3 appears 2 times.
"""

n = 987
count = 0
for i in str(n):
    if n % int(i) == 0:
        count += 1
print(count)
