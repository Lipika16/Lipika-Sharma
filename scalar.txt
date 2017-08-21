#Assignment 6
#NAME: Lipika Sharma
#MATRICULATION NUMBER: 3019922


#Scalar matrix:
def matrix_scalar_mul(m,c):
    """
    Multiplies the matrix m with the scalar c
    >>> matrix_scalar_mul([[1,2,3],[4,5,6]],3)
    [[3, 6, 9], [12, 15, 18]]
    >>> matrix_scalar_mul([[2,3],[4,5]],5)
    [[10, 15], [20, 25]]
    
    """
    n=len(m)
    l=len(m[0])
    d=[[0]*l for _ in range (n)]
    for i in range (n):
        for j in range (l):
            d[i][j]=c*m[i][j] #multiplies each element in the matrix with the scalar
    return d

def main():
   try:
       print("The new matrix after the scalar multiplication is:" ,matrix_scalar_mul([[5,2,5,5],[2,4,4,5]],2))
       print("The new matrix after the scalar multiplication is:" ,matrix_scalar_mul([[5,2,5],[2]],5))
   except IndexError:
       print("Matrix dimensions inconsistent")
   
if __name__ == "__main__":
   import doctest
   doctest.testmod()
   main()

Output:
The new matrix after the scalar multiplication is: [[10, 4, 10, 10], [4, 8, 8, 10]]
Matrix dimensions inconsistent


