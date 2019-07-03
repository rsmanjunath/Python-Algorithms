n= 3
for i in range(n):
    res=1
    x=[0,1,4]
    if x==0:
        print(res)
        continue
    for i in range(1,x+1):
        if(i%2==0):
            res+=1
        elif(i%2==1):
            res*=2
    print(res)