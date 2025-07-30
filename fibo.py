"""
Question: Fibonacci Sequence

Write a program to generate the Fibonacci sequence up to a given number `n`.

Input:
- An integer `n` representing the number of terms in the Fibonacci sequence.

Output:
- A list of integers representing the Fibonacci sequence.

Example:
Input: n = 5
Output: [0, 1, 1, 2, 3]
Explanation:
The first 5 terms of the Fibonacci sequence are 0, 1, 1, 2, 3.
"""

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))

import math

# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):

    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# A utility function to test above functions
for i in range(1,11):
     if (isFibonacci(i) == True):
         print(i,"is a Fibonacci Number")
     else:
         print(i,"is a not Fibonacci Number ")

arr = [1,2,3,4,5]
N = [5]
if not arr:
    print(arr)
print([arr[i % len(arr)] for i in range(N, N + len(arr))])
