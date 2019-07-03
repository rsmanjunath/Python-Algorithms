arr = [1,1, 1, 0, 1, 1, 0, 0, 0, 0]
jump = 2 
energy = 100

for i in range(0,len(arr),jump):
    if arr[i] == 0:
        energy -= 1
    elif arr[i] == 1:
        energy -= 3
print(energy)