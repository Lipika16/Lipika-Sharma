
def strassen_matrix(x,y):
    if len(x) == 1:
        print (x[0] * y[0])
    a = []
    p1 = strassen_matrix(x[0], (y[1] - y[3]))
    p2 = strassen_matrix(y[3], (x[0] + x[1]))
    p3 = strassen_matrix(y[0], (x[2] + x[3]))
    p4 = strassen_matrix(x[3], (y[2] - y[0]))
    p5 = strassen_matrix((x[0] + x[3]), (y[0] + y[3]))
    p6 = strassen_matrix((x[1] - x[3]), (y[2] + y[3]))
    p7 = strassen_matrix((x[0] - x[3]), (y[0] + y[3]))

    a[0] = p5 + p4 - p2 + p6
    a[1] = p1 + p2
    a[2] = p3 + p4
    a[3] = p1 + p5 - p3 - p7

    print (a)
print(strassen_matrix([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]))
