s = "aba"
n = 10

new_s = ""

while n > 0:
    for i in range(len(s)):
        new_s += s[i]
        if len(new_s) == 10:
            break
        else:
            n -= 1
print(new_s)
