"""
Question: Utopian Tree Growth

Write a program to calculate the height of a Utopian tree after a given number of growth cycles. The tree doubles in height during the spring and grows by 1 meter during the summer.

Input:
- An integer `n` representing the number of growth cycles.

Output:
- An integer representing the height of the tree after `n` cycles.

Example:
Input: n = 5
Output: 14
Explanation:
Cycle 1 (spring): Height = 2
Cycle 2 (summer): Height = 3
Cycle 3 (spring): Height = 6
Cycle 4 (summer): Height = 7
Cycle 5 (spring): Height = 14
"""

n= 3
for i in range(n):
    res=1
    x=[0,1,4]
    if x==0:
        print(res)
        continue
    for i in range(1,x+1):
        if(i%2==0):
            res+=1
        elif(i%2==1):
            res*=2
    print(res)