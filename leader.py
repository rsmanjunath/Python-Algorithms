
score = [10,20,40,50,100]
alice = [5,25,50,120]
index = 0
rank_list = []
n = len(score)
r = [5,4,3,2,1]
for i in alice:
    if i >= score[index]:
        rank_list.append(r[index] - 1)
        index += 1
    else:
        rank_list.append(r[index] + 1)
        index += 1

print(rank_list)