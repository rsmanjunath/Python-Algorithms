"""
Question: Armstrong Number

Write a program to check if a given number is an Armstrong number.

Input:
- An integer `num` representing the number to check.

Output:
- A string indicating whether the number is an Armstrong number or not.

Example:
Input: num = 153
Output: "153 is an Armstrong number"
Explanation:
153 = 1^3 + 5^3 + 3^3 = 153
"""

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   print(sum)
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
