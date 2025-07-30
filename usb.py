"""
Question: USB Devices

Write a program to calculate the maximum number of USB devices that can be connected to a computer with a limited number of USB ports and hubs.

Input:
- An integer `ports` representing the number of USB ports on the computer.
- An integer `hubs` representing the number of USB hubs available.
- An integer `devices` representing the total number of USB devices to connect.

Output:
- An integer representing the maximum number of devices that can be connected.

Example:
Input: ports = 4, hubs = 2, devices = 10
Output: 8
Explanation:
Each hub can connect to 4 devices. With 2 hubs, 8 devices can be connected.
"""

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
