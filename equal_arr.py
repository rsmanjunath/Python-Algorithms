arr = [1,1,1,1,1,2,2,4,5,6,7,8]
c = {}
for i in arr:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1
max_val=max(c, key=c.get)

print(len(arr) - c[max_val])
print(c)
