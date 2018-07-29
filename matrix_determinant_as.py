Exercise Sheet 7
Lipika Sharma: lipikasharma@hotmail.com
Arunabh Sharma: arunabhsharma@outlook.com


def matrix_get_submatrix(m,i,j):
    ''' Gives a submatrix from a matrix
        >>> print(matrix_get_submatrix([[0,1,2],[0,3,4],[1,0,2],[2,6,9,0]],0,0))
            [(3, 4), (0, 2), (6, 9)]
        >>> print(matrix_get_submatrix([[0,1],[0,3],[1,0],[2,6]],0,0))
            [(3,), (0,), (6,)]
        >>> matrix_get_submatrix([[6,6,6],[5,5,5],[4,4,4]],2,1)
            [(6, 6), (5, 5)]
    '''
    sub = m[:]              # create submatrix as a copy of m
    
    del(sub[i])             # delete ith row
    sub=list(zip(*sub))     # unzip the list
    
    del(sub[j])             # delete jth column
    sub=list(zip(*sub))     # unzip the list
    
    return sub              # return the submatrix without ith row and jth column


def main():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        main()
print(matrix_get_submatrix([[2,4,6,8],[1,3,5,7],[1,4,7,9],[2,6,9,0]],2,1))
print(matrix_get_submatrix([[2,4],[1,3],[1,4],[2,6]],0,0))
print(matrix_get_submatrix([[4,5,5],[1,2,3],[5,6,7]],1,1))

#Output:
#[(2, 6, 8), (1, 5, 7), (2, 9, 0)]
#[(3,), (4,), (6,)]
#[(4, 5), (5, 7)]

def matrix_det(m):
    '''>>> matrix_det([[1,2,3],[4,5,6],[7,8,9]])
           0
       >>> matrix_det([[1,2],[4,5]])
           -3
       >>> matrix_det([[1,2],[4,5],[7,8]])
           'Matrix does not have proper dimensions. It has to be a square matrix!'
    '''
    rows=len(m)
    cols=len(m[0])    
    
    #check matrix dimensions
    if rows != cols:
        return "Matrix does not have proper dimensions. It has to be a square matrix!"
    
    #base case for 1x1 matrix
    if rows == 1 and cols == 1:
        return m[0][0]
    
    # determinant calculation
    det=0
    for i in range(1):          # first row
        for j in range(cols):   # all columns
            det += ((-1)**(i+j))*m[i][j]*matrix_det(matrix_get_submatrix(m,i,j))
    
    return det
def main():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        main()
print(matrix_det([[5,6],[4,5],[7,9]]))
print(matrix_det([[3,5,6],[6,4,5],[3,7,9]]))
print(matrix_det([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
#Ouput:
#Matrix does not have proper dimensions. It has to be a square matrix!
#-12
#0
