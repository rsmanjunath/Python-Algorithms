a = ["4","3","1","9","6"]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]+a[j] < a[j]+a[i]:
            a[i], a[j] = a[j], a[i]
print(''.join(a))
