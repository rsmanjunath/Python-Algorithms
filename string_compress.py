def compress(string):

    res = ""

    count = 1

    #Add in first character
    

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+= 1
        else:
            res += string[i] + str(count)
            count = 1
                #Ignore if no repeats
    res += string[len(string)-1]+str(count)
            
    return res
print(compress("ddaaafaabbdarrr"))
"""def compress(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return res


print(compress("aabbaaccaad"))"""

