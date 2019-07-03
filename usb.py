def usb(key,drives,b):
    count = []
    for i in range(len(key)):
        for j in range(len(drives)):
            if key[i] + drives[j] <= b:
                count.append(key[i] + drives[j])
    if len(count) == 0:
        return -1
    else:
        return max(count)




print(usb([4],[5], 5))
    