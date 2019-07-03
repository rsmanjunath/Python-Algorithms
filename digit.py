n = 987
count = 0
for i in str(n):
    if n % int(i) == 0:
        count += 1
print(count)
