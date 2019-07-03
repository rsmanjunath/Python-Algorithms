def cutTheSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print(len(arr))
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()
    


sticks = [5,4,4,2,2,8]
print(cutTheSticks(sticks))