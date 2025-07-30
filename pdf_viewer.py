"""
Question: PDF Viewer

Write a program to calculate the area of the highlighted rectangle in a PDF viewer. Each letter has a specific height, and the width of each letter is 1.

Input:
- A list `heights` of 26 integers representing the heights of each letter (a-z).
- A string `word` representing the word to highlight.

Output:
- An integer representing the area of the highlighted rectangle.

Example:
Input: heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], word = "abc"
Output: 9
Explanation:
The heights of 'a', 'b', and 'c' are 1, 3, and 1 respectively. The area is 3 (max height) * 3 (length of word) = 9.
"""

h = [1 ,3, 1, 3, 1, 4, 1]
word = 'abc'
maxi = 0
for i in range(len(word)):
    if(maxi < h[ord(word[i])-97]):
        maxi = h[ord(word[i])-97]
print(maxi*len(word))

