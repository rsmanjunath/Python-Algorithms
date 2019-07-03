

i = 20
j = 23
k = 6
count = 0
for num in range(i, j+1):
    n = (str(num)[::-1])
    if abs(int(n) - num) % k == 0:
        count += 1
print(count)
    
