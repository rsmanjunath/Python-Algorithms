p = 20
d = 3
m = 6
s = 85

count = 0
while s>=p:
    count += 1
    s = s-p
    p = max(p-d,m)

print(count)