def multiply_matrices(m1, m2):
    
    if len(m1) != 2 or len(m2) != 2:
        raise ValueError("Both matrices must have 2 rows")
    if len(m1[0]) != 2 or len(m1[1]) != 2 or len(m2[0]) != 2 or len(m2[1]) != 2:
        raise ValueError("Both matrices must be 2x2")
    
    multiplication = [[0,0],[0,0]] 

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
               multiplication[i][j] += m1[i][k] * m2[k][j]
    return multiplication

m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
multiplication = multiply_matrices(m1, m2)
            
print("First matrix :- ", m1)
print("Second matrix :- ", m2)
print("Matrix multiplication :- ", multiplication)            