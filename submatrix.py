def matrix_get_part(m,i,j,a,b):
    '''
    >>> matrix_get_part(m,2,4,3,6)
    [[4, 5, 6, 7, 8], [4, 5, 6, 7, 8]]
    >>> matrix_get_part(m,1,1,2,2)
    [[1]]
    >>> matrix_get_part(m,2,3,7,8)
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9],
    [3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9]]
    '''
    
    c = (i,i+a-1)
    d = (j,j+b-1)
    
    f = [m[k][d[0]:d[1]] for k in range(len(m))][c[0]:c[1]]

    return f
m=[list(range(10)) for i in range(10)]
def main():
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        main()
print(matrix_get_part(m,2,5,3,7))
print(matrix_get_part(m,3,3,4,4))
print(matrix_get_part(m,4,3,9,6))

Output:
[[5, 6, 7, 8, 9], [5, 6, 7, 8, 9]]
[[3, 4, 5], [3, 4, 5], [3, 4, 5]]
[[3, 4, 5, 6, 7], [3, 4, 5, 6, 7],
 [3, 4, 5, 6, 7], [3, 4, 5, 6, 7],
 [3, 4, 5, 6, 7], [3, 4, 5, 6, 7]]
