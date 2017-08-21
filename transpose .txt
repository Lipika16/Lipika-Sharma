#Transpose matrix:
def matrix_transpose(m):
    """
    Gives the transpose of the matrix
    
    >>> matrix_transpose([[1,2], [3,4]])
    [[1, 3], [2, 4]]
    >>> matrix_transpose([[1,2,3], [3,4,5]])
    [[1, 3], [2, 4], [3, 5]]
    
    """
    n=len(m)  #rows
    l=len(m[0]) #columns
    c=[[0]*n for _ in range (l)] #forms a new matrix with 0 elements
    for i in range (l):
        for j in range (n):
            if i==j:
                c[i][j]=m[i][j] #keeps the same elemets if i is equal to j
            else:
                c[i][j]=m[j][i] #forms a transpose matrix
    return c


def main():
    m=[[1,2,3,5], [3,7,5,9]]
    try:
        print("The transpose of m matrix is :", matrix_transpose(m))
        print("The transpose of m matrix is :", matrix_transpose([[8,9,5],[2,6,7]]))
        print("The transpose of m matrix is :", matrix_transpose([[8,9,5],[2,7]]))
    except IndexError:
        print("Matrix dimensions inconsistent")
   
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

Output:
The transpose of m matrix is : [[1, 3], [2, 7], [3, 5], [5, 9]]
The transpose of m matrix is : [[8, 2], [9, 6], [5, 7]]
Matrix dimensions inconsistent


