def matrix_sub(a,b):
    '''Takes two matrixes and subtracts them.
       Example:
        >>> matrix_sub([[5,6],[3,4]],[[4,5],[2,3]])
            [[1, 1], [1, 1]]
        >>> matrix_sub([[5,6,4],[3,4,2],[6,7,8]],[[4,5,4],[2,3,6],[2,5,7]])
            [[1, 1, 0], [1, 1, -4], [4, 2, 1]]
        >>> matrix_sub([[5,6,4],[6,7,8]],[[4,5,4],[2,3,6]])
            [[1, 1, 0], [4, 4, 2]] 
        '''
    m = len(a)  # number of rows
    n = len(a[0])  # number of cols
    o = len(b)
    p = len(b[0])
    c = [[0] * n for _ in range(m)]
    if m==o and n==p:
        for i in range(m):
            for j in range(n):
                c[i][j] = a[i][j] - b[i][j]
        return c
    else:
        raise IndexError
def main():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        main()
print(matrix_sub([[10, 11, 12],[13, 14, 15],[16, 17, 18]],[[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print(matrix_sub([[10, 11, 12],[13, 14, 15]],[[1, 2, 3],[4, 5, 6]]))
print(matrix_sub([[10, 11],[13, 14]],[[1, 2]]))

#Output:
#[[9, 9, 9], [9, 9, 9], [9, 9, 9]]
#[[9, 9, 9], [9, 9, 9]]
#[[9, 9], [9, 9]]
