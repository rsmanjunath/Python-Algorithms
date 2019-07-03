

def sockMerchant(n, ar):
    z = list()
    lst = list()
    counts = dict()

    numb = ar.split()
    for num in numb:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    for k, v in counts.items():
        if (v > 2 and v % 2 != 0):
            lst.append(v - 1) / 2
        elif (v > 2 and v % 2 ==0):
            lst.append(v / 2)
        elif v > 1:
            lst.append(v / 2)
        elif v == 1:
            z.append(v)
    return(len(lst))
n = input("enter:")
ar = input("enter:")
result = sockMerchant(n, ar)
print(result)
