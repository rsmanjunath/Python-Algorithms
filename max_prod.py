arr = [[1,2,3],[4,5,6],[7,8,9]]
m = 3
n = 3

for i in range(1,m):
    arr[0][i] = arr[0][i-1] * arr[0][i]
for j in range(1,n):
    arr[j][0] = arr[j-1][0] * arr[j][0]
for k in range(1,m):
    for l in range(1,n):
        arr[k][l] = arr[k][l-1] * arr[k][l]
print(arr[m-1][n-1])


