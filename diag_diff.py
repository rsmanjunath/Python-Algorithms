"""
Question: Diagonal Difference

Write a program to calculate the absolute difference between the sums of the diagonals of a square matrix.

Input:
- A 2D list `matrix` representing the square matrix.

Output:
- An integer representing the absolute diagonal difference.

Example:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: 0
Explanation:
Primary diagonal sum = 1 + 5 + 9 = 15
Secondary diagonal sum = 3 + 5 + 7 = 15
Absolute difference = |15 - 15| = 0
"""

def difference(arr, n): 
  
    # Initialize sums of diagonals 
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
      
        for j in range(0, n): 
          
            # finding sum of primary diagonal 
            if (i == j): 
                d1 += arr[i][j] 
  
            # finding sum of secondary diagonal 
            if (i == n - j - 1):
                 
                d2 += arr[i][j] 
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2); 
  
# Driver Code 
n = 4
  
arr = [[11, 2, 4,5], 
       [4 , 5, 6,7], 
       [10, 8, -12,8],
       [2,4,6,7]] 
  
print(difference(arr, n))