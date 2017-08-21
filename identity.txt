#Assignment 6
#NAME: Lipika Sharma
#MATRICULATION NUMBER: 3019922





# Identity Matrix
def matrix_id(d):
    '''
    Gives an identity matrix with the provided dimensions, d
    >>> matrix_id(2)
    [[1, 0], [0, 1]]
    >>> matrix_id(4)
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    '''

    c=[[0]*d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            if i==j:
                c[i][j]=1   #Equates 0 to 1 if i==j
    return c
def main():
    d=3
    print("Identity matrix :" , matrix_id(d))
   
if __name__ == "__main__":
   import doctest
   doctest.testmod()
   main()
   
#Identity matrix : [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
