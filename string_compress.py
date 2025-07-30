"""
Question: String Compression

Write a program to compress a string such that consecutive repeated characters are replaced with the character followed by the count of repetitions.

Input:
- A string `string` consisting of lowercase English letters.

Output:
- A compressed string where repeated characters are represented as `character + count`.

Example:
Input: string = "aabbaaccaad"
Output: "a2b2a2c2a2d1"
Explanation:
The string "aabbaaccaad" is compressed to "a2b2a2c2a2d1" by replacing consecutive repeated characters with their counts.
"""

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

