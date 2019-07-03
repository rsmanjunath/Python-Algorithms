
h = [1 ,3, 1, 3, 1, 4, 1]
word = 'abc'
maxi = 0
for i in range(len(word)):
    if(maxi < h[ord(word[i])-97]):
        maxi = h[ord(word[i])-97]
print(maxi*len(word))

    