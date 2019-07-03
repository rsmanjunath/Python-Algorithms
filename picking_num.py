arr = [1,1,2,2,4,4,5,5,5]

maximum = 0
diff = 1

for k in arr:
    n1 = arr.count(k)
    n2 = arr.count(k-diff) #find number of respective values with given difference.
    print(n2)
    maximum = max(maximum, n1+n2)