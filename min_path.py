arr = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]
m = 3
n = 4

for i in range(1,m):
    arr[0][i] = arr[0][i-1] + arr[0][i]
for j in range(1,n-1):
    arr[j][0] = arr[j-1][0] + arr[j][0]
for k in range(1,m):
    for l in range(1,n):
        arr[k][l] = arr[k][l] + min(arr[k-1][l],arr[k][l-1])
print(arr[m-1][n-1])


