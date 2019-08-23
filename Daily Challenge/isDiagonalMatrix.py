#Check if the given matrix is diagonal
#In linear algebra, a square matrix is called a diagonal matrix if all entries outside the main diagonal are zero.

#Solution
def isDiagonalMatrix(m):
    n = len(m)
    for i in range(0,n): 
        for j in range(0,n): 
            if ((i != j)  and (m[i][j] != 0)):
                return False   
    return True