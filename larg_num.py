s = [78,890,678,6778,45]
a = [str(i) for i in s]

for i in range(len(a)-1):

    for j in range(i+1, len(a)):
        if a[i]+a[j] < a[j]+a[i]:
            a[i], a[j] = a[j], a[i]
            
print("".join(a))