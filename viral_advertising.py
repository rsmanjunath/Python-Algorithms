n = 3
likes = 0
rece = 5
cumu = 0
for i in range(0, n):
    likes = rece // 2
    cumu += likes
    rece = likes * 3

print(cumu)
