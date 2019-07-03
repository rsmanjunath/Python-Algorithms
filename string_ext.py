s = "aabbaabaa"
n = 20
str1 = " "
while n > 0:
    k = n
    for i in range(len(s)):
        str1 += s[i]
        
    k -= 1

print(str1)
    



