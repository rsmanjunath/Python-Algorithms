n = [[1,2,3],[4,5,6],[7,8,9]]
left_to_right = True
for i in range(len(n)):
    if (left_to_right):
        for j in range(len(n)):
            print(n[i][j],end = " ")
    else:
        for j in range(len(n)-1,-1,-1):
            print(n[i][j],end = " ")
    left_to_right = not left_to_right