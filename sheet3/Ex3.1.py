import numpy as np
# def create_matrix(n,m):
#     d2_list = np.zeros((n,m))
#     return d2_list

def create_matrix(n,m):
    d2_list = np.ones((n,m))
    return d2_list

def f(x):
    return (2 * x) + 1
def h(x):
    return 3 * x

def matrix_apply(func, m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = func(m[i][j])

    return m 

matrix =  [[5,2],[3,3]]
print(matrix_apply(f, matrix))
# OUT : [[11, 5], [7, 7]]

a = create_matrix(5,5)
b = create_matrix(5,5)
a = matrix_apply(f , a)
b = matrix_apply(h , b)

def matrix_multiply(a, b): # takes two matrices a and b
    # number of columns in the first matrix must equal the number of rows in the second matrix`
    multiplied_matrix = []
    for i in range(len(a)): # rows of a
        res = []
        for j in range(len(b[0])): # columns of b
            ssum = 0
            for k in range(len(a[0])): # columns of a 
                ssum += a[i][j] * b[k][j]  # equation
            res.append(ssum)
        multiplied_matrix.append(res) 

    return multiplied_matrix
    
mult_matrix = matrix_multiply(a, b)
print(mult_matrix)

    


