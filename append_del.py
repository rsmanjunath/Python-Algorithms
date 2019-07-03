"""Append and Delete 
You have a string, s, of lowercase English alphabetic letters. You can perform two types of operations on s:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly kof the above operations on s. If it’s possible, print Yes; otherwise, print No.

Input Format


The first line contains a string, s, denoting the initial string.
The second line contains a string, t, denoting the desired final string. The third line contains an integer, k, denoting the desired number of operations.

Constraints
1<=|s|<=100 1<=|t|<=100 1<=k<=100 s and t consist of lowercase English alphabetic letters. Output Format Print Yes if you can obtain string by performing exactly operations on ; otherwise, print No. Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes
Explanation 0

We perform delete operations to reduce string s to hacker. Next, we perform append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert s to t by performing exactly k=9 operations, we print Yes."""




s = "hackerhappy"
t = "hackerrank"
k = 9 
s_length = len(s)
t_length = len(t)

if s_length + t_length < k:
        print('Yes') 

same = 0
for s_l, t_l in zip(s, t):
    
    if s_l == t_l: 
        same += 1
    else: 
        break

extra_s = s_length - same
extra_t = t_length - same
difference = extra_s + extra_t
print(extra_s,extra_t,difference)

if difference <= k and difference % 2 == k % 2: 
    print('Yes')
else:
    print('No')

