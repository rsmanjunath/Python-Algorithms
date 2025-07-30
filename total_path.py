"""
Question: Total Path Sum

Write a program to calculate the total sum of all paths from the root to the leaves in a binary tree.

Input:
- A binary tree represented as a nested list or nodes.

Output:
- An integer representing the total sum of all paths.

Example:
Input: tree = [5, [3, [2], [4]], [8, [7], [9]]]
Output: 45
Explanation:
The paths are 5 → 3 → 2, 5 → 3 → 4, 5 → 8 → 7, and 5 → 8 → 9. The total sum is 45.
"""

def numberOfPaths(m, n): 
    # Create a 2D table to store 
    # results of subproblems 
    count = [[0]*n]*m
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for i in range(m): 
        count[i][0] = 1; 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for j in range(n): 
        count[0][j] = 1
    
    # Calculate count of paths for other 
    # cells in bottom-up  
    # manner using the recursive solution 
    for i in range(1, m): 
        for j in range(1,n):              
            count[i][j] = count[i-1][j] + count[i][j-1] 
    return count[m-1][n-1] 
  
# Driver program to test above function  
m = 3
n = 3
print( numberOfPaths(m, n))
