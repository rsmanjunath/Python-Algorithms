arr[n][c] = []

def knap(n,c):
    if arr[n][c] != []:
        return arr[n][c]
    if n == 0 or c == 0:
        result = 0
    elif weight[n] > c:
        result = knap(n-1,c)
    else:
        temp1 = knap(n-1,c)
        temp2 = value[n] + knap(n-1,c-weight[n])
        result = max(temp1,temp2)
    return result

weight = [1,2,4,2,5]
value = [5,3,5,3,2]
n = len(weight)
c = 10
print(knap(4,10))
        

