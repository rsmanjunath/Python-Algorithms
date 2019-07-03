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
  