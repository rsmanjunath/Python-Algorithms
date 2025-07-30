"""
Question: Sock Merchant

Write a program to find the number of matching pairs of socks in a pile.

Input:
- An integer `n` representing the number of socks.
- A list `ar` of integers representing the colors of the socks.

Output:
- An integer representing the number of matching pairs of socks.

Example:
Input: n = 7, ar = [1, 2, 1, 2, 1, 3, 2]
Output: 2
Explanation:
There are two pairs of socks: one pair of color 1 and one pair of color 2.
"""

def sockMerchant(n, ar):
    z = list()
    lst = list()
    counts = dict()

    numb = ar.split()
    for num in numb:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    for k, v in counts.items():
        if (v > 2 and v % 2 != 0):
            lst.append(v - 1) / 2
        elif (v > 2 and v % 2 ==0):
            lst.append(v / 2)
        elif v > 1:
            lst.append(v / 2)
        elif v == 1:
            z.append(v)
    return(len(lst))
n = input("enter:")
ar = input("enter:")
result = sockMerchant(n, ar)
print(result)
